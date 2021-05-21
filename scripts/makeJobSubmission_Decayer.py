#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
from collections import OrderedDict

outputDirectoryBase = "/storage/user/sixie/data/llp_gen"
Base_DIR = "/storage/user/sixie/LLP-Reinterpretation/"
#Base_DIR = "/afs/cern.ch/work/s/sixie/public/Generator/LLP-Reinterpretation"

tarballfile = "/storage/user/sixie/LLP-Reinterpretation/tarball/Decayer_Delphes_tarball.tgz"

datasetList = OrderedDict()
datasetList['ggH_HtoS1S2_S1andS2_55GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_55dot0_AllToTauTau.txt",500]
#datasetList['ggH_HtoS1S2_S1andS2_1GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_1dot0.txt",500]
#datasetList['ggH_HtoS1S2_S1andS2_15GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_15dot0.txt",500]
#datasetList['ggH_HtoS1S2_S1andS2_25GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_25dot0.txt",500]
#datasetList['ggH_HtoS1S2_S1andS2_40GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_40dot0.txt",500]
#datasetList['ggH_HtoS1S2_S1andS2_7GeV_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]
#datasetList['walp_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]
#datasetList['zalp_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]
#datasetList['gammaalp_2Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]
#datasetList['ggalp_3Jets'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]
#datasetList['vv_vv'] = ["/storage/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/",500]




for datasetName in datasetList.keys():
    
    print "Preparing workflow for dataset :" + datasetName + "\n"
   
    outputDirectory = outputDirectoryBase + "/" + datasetName + "/"  
    decayTableFile = datasetList[datasetName][0]
    numberOfJobs = datasetList[datasetName][1] 

    #####################################
    #create run script and executable
    #####################################
    #print ("cat " + Base_DIR + "/condor/" + datasetName + "/run_template.sh" + " | sed 's/XX_MODELNAME_XX/" + datasetName + "/g' " + " | sed 's/XX_DECAYTABLE_XX/" + decayTableFile + "/'" + " | sed 's/XX_OUTPUTDIR_XX/" + outputDirectory + "\//'" +  " > " + Base_DIR + "/condor/" + datasetName + "/run_job.sh")
    os.system("mkdir -p " + Base_DIR + "/condor/" + datasetName + "/log/" )
    os.system("mkdir -p " + Base_DIR + "/condor/" + datasetName + "/out/" )
    os.system("mkdir -p " + Base_DIR + "/condor/" + datasetName + "/err/" )
    os.system("cp " + Base_DIR + "/scripts/run_decayer_job_caltech_tier2.sh " +  Base_DIR + "/condor/" + datasetName + "/run_template.sh")
    os.system("cat " + Base_DIR + "/condor/" + datasetName + "/run_template.sh" + " | sed 's/XX_MODELNAME_XX/" + datasetName + "/g' " + " | sed 's/XX_DECAYTABLE_XX/" + decayTableFile.replace("/","\/") + "/'" + " | sed 's/XX_OUTPUTDIR_XX/" + outputDirectory.replace("/","\/") + "\//'" +  " > " + Base_DIR + "/condor/" + datasetName + "/run_job.sh")
  
    #####################################
    #Create Condor JDL file
    #####################################
    tmpCondorJDLFile = open(Base_DIR + "/condor/" + datasetName + "/task.jdl","w+")
    tmpCondorJDLFileTemplate = """
Universe  = vanilla
Executable = ./run_job.sh
"""
    tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
    tmpCondorJDLFile.write("Arguments = $(I)" + "\n")

    tmpCondorJDLFileTemplate = """
Log = log/job.$(Cluster).$(Process).log
Output = out/job.$(Cluster).$(Process).out
Error = err/job.$(Cluster).$(Process).err
x509userproxy = $ENV(X509_USER_PROXY)
"""
    tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
    tmpCondorJDLFile.write("Transfer_Input_Files = " + tarballfile + ", " + Base_DIR + "/condor/" + datasetName + "/run_job.sh " + "\n")

    tmpCondorJDLFileTemplate = """
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Requirements=(TARGET.OpSysAndVer=="CentOS7" && regexp("blade.*", TARGET.Machine))
RequestMemory = 2000
RequestCpus = 1
RequestDisk = 4
+RunAsOwner = True
+InteractiveUser = true
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006
+SingularityBindCVMFS = True


"""
    tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)

    tmpCondorJDLFileTemplate = """

# Jobs selection
Queue I from (
"""

    tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
    for i in range(0,numberOfJobs):
        tmpCondorJDLFile.write(str(i)+"\n")
    tmpCondorJDLFile.write(")\n")
    tmpCondorJDLFile.close()

