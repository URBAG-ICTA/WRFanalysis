import pandas as pd
import numpy as np
from netCDF4 import Dataset

from PolutantsTable import PolutantsTable as pt


class DataManager:
    # originalDF conté el dataframe amb les dades baixades de la XVPCA
    # Ex: data/AirQualityData/QualitatAire2016TotCatalunya2016.csv
    originalDF = pd.DataFrame()
    
    '''
    dicctionary that stores a dataframe for each polutant in the originalDF
    '''
    by_polutant_dataframes = {}
    
    wrf_files_path = 'D:\\URBAG\\Simulation\\'

    def load_original_file(self, original_file):
        '''
        reads a CVS file in the XVPCA format where the column DATA is parsed as datetime
        '''
        dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
        self.originalDF = pd.read_csv(original_file, parse_dates=['DATA'], date_parser=dateparse)

    
    def list_all_polutants(self):
        '''
        returns an array with all pollutants in the originalDF
        '''
        return self.originalDF['CONTAMINANT'].unique()
    
    
    def list_all_stations(self):
        '''
        returns an array with all stations in the originalDF
        '''
        return self.originalDF['NOM ESTACIO'].unique()
    
    def filter_by_time(self, start_date, end_date):
        '''
        filter originalDF by a range of dates in YYYY-MM-DD format
        '''
        result = self.originalDF[(self.originalDF['DATA'] >= start_date) & (self.originalDF['DATA'] <= end_date)]
        return result

    def filter_by_polutant(self, polutant):
        '''
        return a dataframe with all raws in the originalDF matching the given polutant
        '''
        return self.originalDF[ self.originalDF["CONTAMINANT"] == polutant ]
    
    def split_by_polutant(self):
        '''
        sets the dictionary by_polutant_dataframes with a dataframe for each polutant in the originalDF
        returns this dictionary
        '''
        response = {}
        for element in self.list_all_polutants():
            response[element] = self.filter_by_polutant(element)
        self.by_polutant_dataframes = response
        return response
    
    
    def convert_polutant_dfs_from_xvpca_to_observations(self):
        '''
        converts each dataframe in by_polutant_dataframes from the xvpca
        format to the observations format with on row per observation
        '''        
        for key in self.by_polutant_dataframes:
            superTable = []
            for index, r in self.by_polutant_dataframes[key].iterrows():
                table = self.originalRowToObservations(
                    r['CODI EOI'], r['CODI INE'], r['NOM ESTACIO'], r['AREA URBANA'],
                    r['MUNICIPI'], r['LATITUD'], r['LONGITUD'], r['ALTITUD'], r['DATA'],
                    r['01h'],
                    r['02h'],
                    r['03h'],
                    r['04h'],
                    r['05h'],
                    r['06h'],
                    r['07h'],
                    r['08h'],
                    r['09h'],
                    r['10h'],
                    r['11h'],
                    r['12h'],
                    r['13h'],
                    r['14h'],
                    r['15h'],
                    r['16h'],
                    r['17h'],
                    r['18h'],
                    r['19h'],
                    r['20h'],
                    r['21h'],
                    r['22h'],
                    r['23h'],
                    r['24h'])
                if table != False:
                    superTable = superTable+table
            self.by_polutant_dataframes[key] = pd.DataFrame(superTable,columns =['CODI EOI', 'CODI INE', 'NOM ESTACIO', 'AREA URBANA',
                                                                                 'MUNICIPI', 'LATITUD', 'LONGITUD', 'ALTITUD', 'DATA',
                                                                                 'YEAR', 'MONTH', 'DAY',
                                                                                 'HOUR','OBSERVATION'])
        return self.by_polutant_dataframes
    
    def originalRowToObservations(self, codi_eoi, codi_municipi, nom_estacio, area_urbana,                            
                                  municipi, latitud, longitud, altitud, data,
                                  H01, H02, H03, H04,
                                  H05, H06, H07, H08,
                                  H09, H10, H11, H12,
                                  H13, H14, H15, H16,
                                  H17, H18, H19, H20,
                                  H21, H22, H23, H24
                                  ):
        '''
        for each row in the xvpca format return a row in the observation format
        '''
        table = []
        baseRow = [codi_eoi, codi_municipi, nom_estacio, area_urbana,
                   municipi, latitud, longitud, altitud, data,
                   data.year, data.month, data.day]

        newValues = [1, H01]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [2, H02]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [3, H03]
        newRow = baseRow + newValues
        table.append(newRow)            

        newValues = [4, H04]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [5, H05]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [6, H06]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [7, H07]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [8, H08]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [9, H09]
        newRow = baseRow + newValues
        table.append(newRow)            

        newValues = [10, H10]
        newRow = baseRow + newValues
        table.append(newRow)                



        newValues = [11, H11]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [12, H12]
        newRow = baseRow + newValues
        table.append(newRow)             

        newValues = [13, H13]
        newRow = baseRow + newValues
        table.append(newRow)

        newValues = [14, H14]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [15, H15]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [16, H16]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [17, H17]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [18, H18]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [19, H19]
        newRow = baseRow + newValues
        table.append(newRow) 

        newValues = [20, H20]
        newRow = baseRow + newValues
        table.append(newRow)             

        newValues = [21, H21]
        newRow = baseRow + newValues
        table.append(newRow)   

        newValues = [22, H22]
        newRow = baseRow + newValues
        table.append(newRow)   

        newValues = [23, H23]
        newRow = baseRow + newValues
        table.append(newRow)   

        newValues = [00, H24]
        newRow = baseRow + newValues
        table.append(newRow)               

        if table == []:
            return False
        return table


    def add_simulated_values_to_by_polutant_dataframes(self, polutant, model_prefix):
        '''
        Adds four columns to the dataframe of each polutant
        Temperature in celcius: [model_prefix]_T_celcius
        Presure: [model_prefix]_P
        Concentration in ppmv: [model_prefix]_[polutant]_ppmv
        Concentration in ug/m3: [model_prefix]_[polutant]_ug/m3
        This function is ready to work with:
        NO
        NO2
        O3
        PM10
        PM2.5
        SO2
        '''
        df = self.by_polutant_dataframes[polutant]

        predVariableOriginalUnits = model_prefix+'_'+pt.AllPollutants[polutant]['name']+'_'+pt.AllPollutants[polutant]['wrf_units']
        predTemperature = model_prefix+'_'+'T_celcius'
        predPressure = model_prefix+'_'+'P'
        predVariableTransformet = model_prefix+'_'+pt.AllPollutants[polutant]['name']+'_'+pt.AllPollutants[polutant]['obs_units']
        
        df[predVariableOriginalUnits] = np.nan
        df[predTemperature] = np.nan
        df[predPressure] = np.nan
        df[predVariableTransformet] = np.nan
        
        for index, r in df.iterrows():
            values = self.getPredictedValue(r['LATITUD'], r['LONGITUD'], r['YEAR'], r['MONTH'], r['DAY'], r['HOUR'], polutant, pt.AllPollutants[polutant]['wrf_variable'])
            df.at[index,predVariableOriginalUnits] = values[0]
            df.at[index,predPressure] = values[1]
            df.at[index,predTemperature] = values[2]
            df.at[index,predVariableTransformet] = values[3]

        return df        

    def getPredictedValue(self, lat, lon, year, month, day, hour, polutant, wrf_variable):
        wrf_file = self.wrf_files_path+str(year)+'-'+str(month).zfill(2)+'-'+str(day).zfill(2)+'_'+str(hour).zfill(2)

        wrf_data = Dataset(wrf_file, "r", format="NETCDF3")
    
        XLONG = wrf_data.variables['XLONG'][0]
        XLAT = wrf_data.variables['XLAT'][0]
        distance = abs(XLONG-lon)+abs(XLAT-lat)
        minimumValue = np.amin(distance)
        res = np.where(distance == minimumValue)
    
        wrf_value = wrf_data.variables[wrf_variable][0][0][res[0][0]][res[1][0]]
        wrf_P = wrf_data.variables['P'][0][0][res[0][0]][res[1][0]]
        wrf_PB = wrf_data.variables['PB'][0][0][res[0][0]][res[1][0]]
        wrf_T = wrf_data.variables['T'][0][0][res[0][0]][res[1][0]]
    
        TemperatureCel = self.from_WRFtemp_to_Celcius(wrf_T, wrf_PB, wrf_P)
        
        transformed_wrf_variable = self.fromWRFunitsToObsevationUnits(polutant, wrf_value, wrf_P, wrf_PB, TemperatureCel)        
        
        '''        
        if polutant == 'O3':
            transformed_wrf_variable = self.O3ppmToO3ugm3(wrf_value, wrf_P, wrf_PB, TemperatureCel, 1000)
        '''
        return [wrf_value, wrf_P+wrf_PB, TemperatureCel, transformed_wrf_variable]   

    def from_WRFtemp_to_Celcius(self, wrf_T, wrf_PT, wrf_P):
        theta = wrf_T + 300
        ptot = wrf_P + wrf_PT
        temp = theta*(ptot/100000)**(2/7)
        
        return temp-273.15

    def fromWRFunitsToObsevationUnits(self, polutant, wrf_value, wrf_P, wrf_PB, TempCel):
        if polutant in ['SO2', 'O3', 'NO', 'NO2']:
            R=0.08205746
            Factor = 1000
            polutant_ug_m3 = (wrf_value * pt.AllPollutants[polutant]['molar_mass'] * Factor * ((wrf_P+wrf_PB)/101325 ) ) / (R * (TempCel + 273.15))
            return polutant_ug_m3
        
        if polutant in ['PM10', 'PM2.5']:
            return wrf_value


