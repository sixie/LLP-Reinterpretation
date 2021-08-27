import os
import numpy as np
import math

mX    = np.linspace(250, 3000, 20)
lam   = np.linspace(0, 0, 1) 

output_dir="/storage/af/user/jmina/Plots/Daniel_Plots/Fig5/Plot3_Data_0827/"
mg5_dir = "/storage/af/user/jmina/LLP-Reinterpretation/MG5_aMC_v2_7_3/bin/mg5_aMC"

for m in mX:
	for l in lam:
		output = output_dir + "m" + str(round(m, 2)) +"_l"+ str(l) + '.dat'
		os.system(mg5_dir + " " + output)
