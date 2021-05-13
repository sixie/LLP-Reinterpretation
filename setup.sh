
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
#my_pythia8=/storage/user/cpena/work/new_installation_reinterpret/LLP-Reinterpretation/MG5_aMC_v2_9_3/HEPTools/pythia8/
my_pythia8=${top_dir}/MG5_aMC_v2_9_3/HEPTools/pythia8/
echo ${my_pythia8}
export PYTHIA8DATA=${my_pythia8}/share/Pythia8/xmldoc
echo $PYTHIA8DATA

