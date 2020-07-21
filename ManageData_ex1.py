from src.DataManager import DataManager
from copy import deepcopy
from datetime import datetime

DM = DataManager()

DM.load_original_file("./data/AirQualityData/QualitatAire2016TotCatalunya.csv")

number_polutants = len(DM.list_all_polutants())
number_of_stations = len(DM.list_all_stations())
print('Full file data:')
print('Number of raws in originalDF: {}'.format(len(DM.originalDF)))
print('Number of polutants: {}'.format(number_polutants))
print('Number of stations: {}'.format(number_of_stations))
print('\n\n----------------------\n\n')

original_data_frame = DM.originalDF

DM.originalDF = DM.filter_by_time('2016-07-01', '2016-07-15')

number_polutants = len(DM.list_all_polutants())
number_of_stations = len(DM.list_all_stations())
print('Filteed by time data:')
print('Number of raws in originalDF: {}'.format(len(DM.originalDF)))
print('Number of polutants: {}'.format(number_polutants))
print('Number of stations: {}'.format(number_of_stations))

DM.split_by_polutant()

PolutantsDF_xvpca_format = deepcopy(DM.by_polutant_dataframes)

DM.convert_polutant_dfs_from_xvpca_to_observations()

PolutantsDF_observations_format = DM.by_polutant_dataframes


print('start SO2 at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('SO2', 'M')

print('start O3 at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('O3', 'M')

print('start NO at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('NO', 'M')

print('start NO2 at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('NO2', 'M')

print('start PM10 at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('PM10', 'M')

print('start PM2.5 at: {}'.format(datetime.now()))
DM.add_simulated_values_to_by_polutant_dataframes('PM2.5', 'M')

# Save DM.by_polutant_dataframes in csv files
for key in DM.by_polutant_dataframes:
    DM.by_polutant_dataframes[key].to_csv('./data/AirQualityData/polutants/'+key+'_2016-07.csv')
    
    

