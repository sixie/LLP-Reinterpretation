plotscriptdata_0803.py is meant to generate data through Madgraph for gluon fusion di-Higgs processes over some parameter space where the varied parameters are the mass of the bSM Higgs and the coupling parameter between the heavy Higgs and down and antidown quarks (lambda). The file may be editted to reflect different parameter spaces. The script will write .dat files that will be run in Madgraph.

run_plotscriptdata_0803.py runs the .dat files produced by plotscriptdata.py according to the same parameter space.

To run:
python2 plotscriptdata_0803.py
python2 run_plotscriptdata_0803.py

data_parser_0803.py and data_parser_0809.py are two versions of a data parser meant to skim through the data produced in the preceding simulation runs and provide data points with lambda, mass, and cross section values. Run in notebook.

Plot3_0805.ipynb and Plot3_0807.ipynb are two plotting. notebooks that use the data parsers and earlier data to make plots of the simulated process data.
