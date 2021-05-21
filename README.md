# LLP-Reinterpretation

  Repository to install Madgraph5, Pythia8 and Delphes to perform LHC re-interpretations

# Installation
```
git clone git@github.com:cmorgoth/LLP-Reinterpretation.git
cd LLP-Reinterpretation
./install.sh
```

# Installing Pythia Decayer
```
git clone git@github.com:LLP-LHC/Pythia8Decayer.git
```

have a clean .bash_profile
got to cmssw 9_4_20, do cmsenv
source the new setup.sh
then the cmake3 thing
then make.

On Caltech Tier2 (login-1.hep.caltech.edu), have only the following lines in your .bash_profile setup:
```
export SCRAM_ARCH=slc7_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
export X509_USER_PROXY=/storage/user/sixie/x509_proxy
```

Set up cmssw software stack:
```
cmsrel CMSSW_9_4_20
cd  CMSSW_9_4_20
cmsenv
cd -
```

source the setup script:
```
source setup.sh
```

compile Pythia8Decayer:
```
mkdir Pythia8Decayer_build
mkdir Pythia8Decayer_install
cd Pythia8Decayer_build
cmake3 -DCMAKE_INSTALL_PREFIX=../Pythia8Decayer_install ../Pythia8Decayer -DBOOST_ROOT=../MG5_aMC_v2_9_3/HEPTools/boost/
make
```
