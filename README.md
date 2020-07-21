# WRFanalysis
This project provides a set of functionalities to evaluate
WRF simulation output and compare them with physical observations.

1. Datamanagement
The DataManager Component allows to transform the data acquired from
Xarxa de Vigilància i Previsió de la Contaminació (XVPCA) and then add
to it a column with the corresponding predictions for each variable made 
by a WRF-CHEM model.
Once the Data is in the correct format:

2. URBAGgraphs
The URBAGgraphs component allows to create several plots to quickly analyze
and compare simulations vs real data.

Thera are also some scripts to show how to use each of the components
1. ManageData_ex1.py
2. GraphExamples.py

Notice that the use of ManageData will require to have available a wrf-chem
simulation as well as observation on Air Quality.
We provide a csv file with all data on air quality for 2016 in Catalonia
in the folder data/AirQualityData/QualitatAire2016TotCatalunya.csv

Since the wrf-chem outputs are too large to be part of this repository
some sample files have been created in order to use the module for graphics.
Those can be found at data/AirQualityData/example_01
If you are interested on having a sample simulation you can contact 
marcel.serra@uab.cat

