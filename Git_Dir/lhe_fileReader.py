# LHE File Reader
# Coders: Nathan Suri, Caltech
#         Joseph Mina, Caltech
# Version 1: July 4, 2020
# Version 2: June 16, 2021
# Version 3: Septermber 10, 2021
# LPC LLP Group

# Description
# Extract 4-momenta information from LHE files

# Action Plan
# Clean/consolidate codebase

# Imports

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np
import ROOT as rt
import os
import shlex
import uproot
import datetime
import pytz
import time

# Fundamental Constants (SI)

c = 3 * 10 ** 8
h_bar = 6.582119569 * 10 ** -25

# Calculation Functions

def pt_calc(px, py):
    return np.sqrt(px**2+py**2)

def pmag_calc(momentum):
    return np.linalg.norm(momentum)

def eta_calc(momentum):
    mom_mag = np.linalg.norm(momentum)
    co = momentum[2] / mom_mag
    pseudo = -np.log(np.sqrt((1 - co)/(1 + co)))
    return pseudo

def phi_calc(momentum):
    if momentum[0] < 0 and momentum[1] > 0:
        phi = np.arctan(momentum[1]/momentum[0]) + np.pi
    elif momentum[0] < 0 and momentum[1] < 0:
        phi = np.arctan(momentum[1]/momentum[0]) - np.pi
    else:
        phi = np.arctan(momentum[1]/momentum[0])
    return phi

def rapid_calc(momentum, energy):
    rapid = 0.5 * np.log((energy + momentum[2])/(energy - momentum[2]))
    return rapid

# Converts 4-momenta into velocities
def p4_to_velo(p4Array, mass, energy):
    # Checks for zero 4-momenta
    if(np.linalg.norm(p4Array) == 0):
      velo = np.array([0, 0, 0])
    else:
      velo = p4Array / energy
    return velo

# Returns kinematic information from LHE event information
def quirkP4extract_MC(line):
    higgs_1 = line[0]
    higgs_2 = line[1]
    higgs_3 = line[2]
    
    three_momentum_h1 = np.array([float(higgs_1[6]), float(higgs_1[7]), float(higgs_1[8])])
    mass_h1 = float(higgs_1[10])
    energy_h1 = float(higgs_1[9])
    v_h1 = p4_to_velo(three_momentum_h1, mass_h1, energy_h1)
    
    three_momentum_h2 = np.array([float(higgs_2[6]), float(higgs_2[7]), float(higgs_2[8])])
    energy_h2 = float(higgs_2[9])
    mass_h2 = float(higgs_2[10])
    v_h2 = p4_to_velo(three_momentum_h2, mass_h2, energy_h2)
    
    three_momentum_h3 = np.array([float(higgs_3[6]), float(higgs_3[7]), float(higgs_3[8])])
    energy_h3 = float(higgs_3[9])
    mass_h3 = float(higgs_3[10])
    v_h3 = p4_to_velo(three_momentum_h3, mass_h3, energy_h3)
    
    pt_h1 = pt_calc(float(higgs_1[6]), float(higgs_1[7]))
    pt_h2 = pt_calc(float(higgs_2[6]), float(higgs_2[7]))
    pt_h3 = pt_calc(float(higgs_2[6]), float(higgs_3[7]))
    
    pmag_h1 = pmag_calc(three_momentum_h1)
    pmag_h2 = pmag_calc(three_momentum_h2)
    pmag_h3 = pmag_calc(three_momentum_h3)
    
    eta_h1 = eta_calc(three_momentum_h1)
    eta_h2 = eta_calc(three_momentum_h2)
    eta_h3 = eta_calc(three_momentum_h3)
    
    rapid_h1 = rapid_calc(three_momentum_h1, energy_h1)
    rapid_h2 = rapid_calc(three_momentum_h2, energy_h2)
    rapid_h3 = rapid_calc(three_momentum_h3, energy_h3)
    
    phi_h1 = phi_calc(three_momentum_h1)
    phi_h2 = phi_calc(three_momentum_h2)
    phi_h3 = phi_calc(three_momentum_h3)

    return v_h1, three_momentum_h1, mass_h1, energy_h1, pt_h1, eta_h1, rapid_h1, phi_h1, pmag_h1, v_h2, three_momentum_h2, mass_h2, energy_h2, pt_h2, eta_h2, rapid_h2, phi_h2, pmag_h2, v_h3, three_momentum_h3, mass_h3, energy_h3, pt_h3, eta_h3, rapid_h3, phi_h3, pmag_h3

# Extracts velocities/masses/energies/pT/etc. for particles in question
def lhe_reader_MC(filename):
    higgsLHEfile = open(filename)
    higgs_arr1 = []
    higgs_arr2 = []
    higgs_arr3 = []
    event_tag = False
    event_arr = []
    for line in higgsLHEfile:
        arrayLine = line.split()
        if "<event>" in line:
            event_tag = True

        elif "</event>" in line:
            event_tag = False
            v1, p_h1, mass_h1, energy_h1, pt_h1, eta_h1, rapid_h1, phi_h1, pmag_h1, v2, p_h2, mass_h2, energy_h2, pt_h2, eta_h2, rapid_h2, phi_h2, pmag_h2, v3, p_h3, mass_h3, energy_h3, pt_h3, eta_h3, rapid_h3, phi_h3, pmag_h3 = quirkP4extract_MC(event_arr)
            higgs_arr1.append([v1, p_h1, mass_h1, energy_h1, pt_h1, eta_h1, rapid_h1, phi_h1, pmag_h1])
            higgs_arr2.append([v2, p_h2, mass_h2, energy_h2, pt_h2, eta_h2, rapid_h2, phi_h2, pmag_h2])
            higgs_arr3.append([v3, p_h3, mass_h3, energy_h3, pt_h3, eta_h3, rapid_h3, phi_h3, pmag_h3])
            event_arr = []

        if event_tag:
        # 25 == Higgs PDGID
            if "25  1    " in line and len(arrayLine) > 5:
                event_arr.append(arrayLine)
    
    higgsLHEfile.close()
    return higgs_arr1, higgs_arr2, higgs_arr3
