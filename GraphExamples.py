from src.URBAGgraphs import URBAGgraphs

ug = URBAGgraphs()

ug.load_file('./data/AirQualityData/example_01/polutantsSO2_2016-07.csv')

DataFrame = ug.df

estacions = ug.listEstacions()

'''Daily Profiles'''

ug.plot_Daily_Profile_Error_Bars('SO2', ['Barcelona (Eixample)'], 'M', error = 'std', description=False)

ug.plot_Daily_Profile_Areas('SO2', ['Barcelona (Eixample)'], 'M', error = '90percentil', description=False)



'''Time Series'''
#newdf = ug.plot_Time_Series_v1('SO2', 'Barcelona (Eixample)', 'M')

#newdf = ug.plot_Time_Series_v2('SO2', 'Barcelona (Eixample)', 'M')


'''Correlations matrices'''
#ug.plot_Station_Correlation('M', 'SO2')


'''Differences matrices'''
#ug.plot_Matrix_Station_vs_Day('M', 'SO2')

#ug.plot_Matrix_Station_vs_Hour('M', 'SO2')

#ug.plot_Matrix_Day_vs_Hour('M', 'SO2')