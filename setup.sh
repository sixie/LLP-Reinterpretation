
#!/bin/sh
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "LINUX"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "MACOS"
  export MACOSX_DEPLOYMENT_TARGET=10.15
fi
#####################
###setup PYTHIA8DATA
#####################
top_dir=`git rev-parse --show-toplevel`
echo ${top_dir}
my_pythia8=${top_dir}/MG5_aMC_v2_9_3/HEPTools/pythia8
echo ${my_pythia8}
export PATH=${my_pythia8}/bin:${PATH}
export PYTHIA8DATA=${my_pythia8}/share/Pythia8/xmldoc
echo $PYTHIA8DATA
#export dir=/storage/user/cpena/work/new_clean_for_llp/CMSSW_9_4_20/src/LLP-Reinterpretation/
export LD_LIBRARY_PATH=${top_dir}/MG5_aMC_v2_9_3/HEPTools/boost/lib:${LD_LIBRARY_PATH}
