import numpy as np

class PolutantsTable:
    
    AllPolutants = {
    'NOX'  :{'name':'NOX',  'file':'2016-07_NOX', 'molar_mass':np.nan, 'wrf_variable':'',          'wrf_units':'',        'obs_units':'ug/m3', 'ready':False},
    'SO2'  :{'name':'SO2',  'file':'2016-07_SO2', 'molar_mass':64.066, 'wrf_variable':'so2',       'wrf_units':'ppmv',    'obs_units':'ug/m3', 'ready':True},
    'O3'   :{'name':'O3',   'file':'2016-07_O3',  'molar_mass':48,     'wrf_variable':'o3',        'wrf_units':'ppmv',    'obs_units':'ug/m3', 'ready':True},
    'NO'   :{'name':'NO',   'file':'2016-07_NO',  'molar_mass':30.01,  'wrf_variable':'no',        'wrf_units':'ppmv',    'obs_units':'ug/m3', 'ready':True},
    'NO2'  :{'name':'NO2',  'file':'2016-07_NO2', 'molar_mass':46.0055,'wrf_variable':'no2',       'wrf_units':'ppmv',    'obs_units':'ug/m3', 'ready':True},
    'PM10' :{'name':'PM10', 'file':'2016-07_PM10','molar_mass':np.nan, 'wrf_variable':'PM10',      'wrf_units':'ug m^-3', 'obs_units':'ug/m3', 'ready':True},
    'CO'   :{'name':'CO',   'file':'2016-07_CO',  'molar_mass':28.01,  'wrf_variable':'co',        'wrf_units':'ppmv',    'obs_units':'mg/m3', 'ready':False},
    'C6H6' :{'name':'C6H6', 'file':'2016-07_C6H6','molar_mass':78.11,  'wrf_variable':'',          'wrf_units':'',        'obs_units':'',      'ready':False},
    'PM2.5':{'name':'PM2.5','file':'2016-07_PM25','molar_mass':np.nan, 'wrf_variable':'PM2_5_DRY', 'wrf_units':'ug m^-3', 'obs_units':'ug/m3', 'ready':True}
    }