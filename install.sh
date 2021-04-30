
#!/bin/sh
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "LINUX"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "MACOS"
  export MACOSX_DEPLOYMENT_TARGET=10.15
fi
####################
#get and install Madgraph5
###################
current_dir=$PWD
wget https://launchpad.net/mg5amcnlo/2.0/2.9.x/+download/MG5_aMC_v2.9.3.tar.gz
tar -zxvf MG5_aMC_v2.9.3.tar.gz
rm MG5_aMC_v2.9.3.tar.gz
cd MG5_aMC_v2_9_3
python2 ./bin/mg5_aMC ${current_dir}/install_scripts/madgraph_install.dat
cd $current_dir
############################
#get and install delphes from CW
############################

wget https://www.dropbox.com/s/fn3gybwb2lftik1/delphes_cp.tar.gz
tar -zxvf delphes_cp.tar.gz
rm delphes_cp.tar.gz
cd Delphes-3.4.2
./configure
make -j 12
cd $current_dir
