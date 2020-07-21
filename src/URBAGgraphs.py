import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from src.PolutantsTable import PolutantsTable as pt

class URBAGgraphs:
    
    df = pd.DataFrame()

    obs_color='blue'
    pre_color='tab:orange'

    def load_file(self, file):
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
        self.df = pd.read_csv(file, parse_dates=['DATA'], date_parser=dateparse)


    def filter_by_time(self, start_date, end_date):
        '''
        filter df by a range of dates in YYYY-MM-DD format
        '''
        result = self.df[(self.df['DATA'] >= start_date) & (self.df['DATA'] <= end_date)]
        return result


    def dailyProfile(self, polutant, estacions, model):

        dailyProfileMean = self.df[self.df['NOM ESTACIO'].isin(estacions)].groupby(by=['HOUR']).mean()
        dailyProfileStd = self.df[self.df['NOM ESTACIO'].isin(estacions)].groupby(by=['HOUR']).std()
        quantile05 = self.df[self.df['NOM ESTACIO'].isin(estacions)].groupby(by=['HOUR']).quantile(0.05)
        quantile95 = self.df[self.df['NOM ESTACIO'].isin(estacions)].groupby(by=['HOUR']).quantile(0.95)
        return dailyProfileMean, dailyProfileStd, quantile05, quantile95


    def plot_Daily_Profile_Error_Bars(self, polutant, estacions, model, filename='./output/DailyProfileErrBars', error = '90percentil', description = False):
        '''
        createds a daily profile plot with the loaded file in the self.df
        indicate pol
        
        error = std / 90percentil
        '''
        
        dp, dpd, q5, q95 = self.dailyProfile(polutant, estacions, model)
        
        hours = dp.index
        
        obs = dp['OBSERVATION']
        pre = dp[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]
        obs_std = dp['OBSERVATION']
        pre_std = dpd[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]

        obs_q5 = q5['OBSERVATION']
        obs_q95 = q95['OBSERVATION']    
        pre_q5 = q5[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]
        pre_q95 = q95[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]

        fig, ax1 = plt.subplots(nrows=1, sharex=True)
        
        if(error == 'std'):
            ax1.errorbar(hours, obs, yerr=obs_std, color=self.obs_color, label="observation", fmt='o')
            ax1.errorbar(hours, pre, yerr=pre_std, color=self.pre_color, label='prediction', fmt='o')
            error_text = 'standard deviation'
        elif(error == '90percentil'):
            ax1.errorbar(hours, obs, yerr=np.vstack([obs_q5, obs_q95]), color=self.obs_color, label="observation", fmt='o')
            ax1.errorbar(hours, pre, yerr=np.vstack([pre_q5, pre_q95]), color=self.pre_color, label='prediction', fmt='o')
            error_text = 'percentil 90'
        
        if description == True:        
            start_date = self.df['DATA'].min()
            end_date = self.df['DATA'].max()
            line1 = 'Daily profile from {start} to {end}.\n'.format(start=start_date, end=end_date)
            line2 = 'The error is given by {error}'.format(error = error_text)
            full_text = line1 + line2
            ax1.text(0,-6,full_text)

        ax1.set_xlabel('hours')
        ax1.set_ylabel('concentration {}'.format(pt.AllPolutants[polutant]['obs_units']) )
        ax1.set_title(str(estacions)+' '+polutant)
        ax1.legend()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        return dp, dpd, q5, q95


    def plot_Daily_Profile_Areas(self, polutant, estacions, model, filename='./output/DailyProfileArea', error = '90percentil', description = False):
        '''
        createds a daily profile plot with the loaded file in the self.df
        indicate pol
        
        error = std / 90percentil
        '''
        
        dp, dpd, q5, q95 = self.dailyProfile(polutant, estacions, model)
        
        hours = dp.index
        
        obs = dp['OBSERVATION']
        pre = dp[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]
        obs_std = dp['OBSERVATION']
        pre_std = dpd[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]

        obs_q5 = q5['OBSERVATION']
        obs_q95 = q95['OBSERVATION']    
        pre_q5 = q5[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]
        pre_q95 = q95[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]

        fig, ax1 = plt.subplots(nrows=1, sharex=True)
        ax1.plot(hours, obs, color='b', label='observation')
        ax1.plot(hours, pre, color='tab:orange', label='prediction')
        
        if(error == 'std'):
            ax1.fill_between(hours, obs+obs_std, obs-obs_std, facecolor='blue', alpha=0.2)
            ax1.fill_between(hours, pre+pre_std, pre-pre_std, facecolors='tab:orange', alpha=0.2)
            error_text = 'standard deviation'
        elif(error == '90percentil'):
            ax1.fill_between(hours, obs+obs_q95, obs-obs_q5, facecolor='blue', alpha=0.2)
            ax1.fill_between(hours, pre+pre_q95, pre-pre_q5, facecolors='tab:orange', alpha=0.2)            
            error_text = 'percentil 90'

        if description == True:        
            start_date = self.df['DATA'].min()
            end_date = self.df['DATA'].max()
            line1 = 'Daily profile {start} / {end}.\n'.format(start=start_date, end=end_date)
            line2 = 'The error is given by {error}'.format(error = error_text)
            full_text = line1 + line2
            ax1.text(1,45,full_text)        

        ax1.set_xlabel('hours')
        ax1.set_ylabel('concentration {}'.format(pt.AllPolutants[polutant]['obs_units']) )      
        ax1.set_title(str(estacions)+' '+polutant)
        ax1.legend()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        return dp, dpd, q5, q95      
        
    def listEstacions(self):
        result = self.df.groupby(by=['NOM ESTACIO','MUNICIPI', 'LATITUD', 'LONGITUD', 'ALTITUD', 'AREA URBANA']).count()[['CODI EOI']]
        return result
    
    
    def timeSeries(self, polutant, estacio, model):
        timeSerieEstacio = self.df[self.df['NOM ESTACIO'] == estacio].sort_values(by=['DATA'])
        return timeSerieEstacio
    

    def plot_Time_Series_v1(self, polutant, estacio, model, filename='./output/Time_Series_1'):
        df = self.timeSeries(polutant, estacio, model)        

        df['DATETIME'] = df.apply(lambda r:
            str(r['YEAR'])+'-'+str(r['MONTH']).zfill(2)+'-'+str(r['DAY']).zfill(2)+' '+str(r['HOUR']).zfill(2)+':00:00',axis=1)   
        df['DATETIME'] = pd.to_datetime(df['DATETIME'], infer_datetime_format=False)
        plt.style.use('ggplot')
        df.plot(x='DATETIME',
                y=['OBSERVATION', model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']],
                figsize=(12,4))
        plt.title(polutant+' '+estacio)
        plt.ylabel('concentration {}'.format(pt.AllPolutants[polutant]['obs_units']) )
        plt.savefig(filename, dpi=300)
        plt.show()
        
        return df
        
    def plot_Time_Series_v2(self, polutant, estacio, model, filename='./output/Time_Series_2'):
        sns.set()
        df = self.timeSeries(polutant, estacio, model)
        df['DATETIME'] = df.apply(lambda r:
                                  str(r['YEAR'])+'-'+str(r['MONTH']).zfill(2)+'-'+str(r['DAY']).zfill(2)+' '+str(r['HOUR']).zfill(2)+':00:00',axis=1)   
        df['DATETIME'] = pd.to_datetime(df['DATETIME'], infer_datetime_format=False)
        
        df.plot(x='DATETIME',
                y=['OBSERVATION',
                   model+'_'+polutant+'_'
                   +pt.AllPolutants[polutant]['obs_units']],
                figsize=(20,10), linewidth=5, fontsize=20)
        plt.title(polutant+' '+estacio)
        plt.ylabel('concentration {}'.format(pt.AllPolutants[polutant]['obs_units']) )
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        
        return df
            
        
    def correlationByStation(self, model, polutant):
        estacions = self.df['NOM ESTACIO'].unique()
        correlations = []
        for estation in estacions:
            estations_df = self.df[self.df['NOM ESTACIO'] == estation]
            correlations.append(estations_df['OBSERVATION'].corr(estations_df[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]))
        return estacions, correlations        
        
    def plot_Station_Correlation(self, model, polutant, filename = './output/Station_Correlation'):
        '''
        Creates a horizontal bar graph with the correlation between
        observation and prediction for each Station

        Parameters
        ----------
        model : TYPE
            DESCRIPTION.
        polutant : TYPE
            DESCRIPTION.
        filename : TYPE, optional
            DESCRIPTION. The default is './output/Station_Correlation'.

        Returns
        -------
        None.

        '''
        estations, correlations = self.correlationByStation(model, polutant)
        plt.rcdefaults()
        fig, ax = plt.subplots(figsize=(15, 15))    
        ax.barh(estations, correlations, height=0.8)
        ax.grid(axis='x')
        ax.set_xlabel('Person Correlation')
        plt.title(polutant+' predicted vs observation Pearson correlation \n from '+self.df['DATA'].min().strftime('%d/%m/%Y')+' to '+self.df['DATA'].max().strftime('%d/%m/%Y'))
        plt.savefig(filename, dpi=300)
        plt.show()          
        

    def plot_Matrix_Station_vs_Day(self, model, polutant, filename = './output/station_vs_day'):
        '''
        Creates a matrix plot based on the df data of Stations vs Days
        
        Parameters
        ----------
        model : string
            Column name in the dataframe df that contains the predicted values
        polutant : string
            polutant that is beiing ploted its main use is in the title            
        filename : string, optional
            path where the plot will be save in png format    
            The default is './output/station_vs_day'
            

        Returns
        -------
        pivot_df : dataframe
            table build to plot the data in case it needs to be reused o reviewed
            
        '''
        
        self.df['correlation'] = self.df[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]-self.df['OBSERVATION']
        pivot_df = self.df.pivot_table(values='correlation', index='NOM ESTACIO', columns='DAY')
        plt.figure(figsize=(10,10))
        sns.set_context(font_scale=2)
        plt.title(polutant+' predicted-observed concentration \n Station vs Day; from '+self.df['DATA'].min().strftime('%d/%m/%Y')+' to '+self.df['DATA'].max().strftime('%d/%m/%Y'))
        sns.heatmap(pivot_df, cmap='coolwarm', center=0)
        plt.savefig(filename, dpi=300)
        plt.show() 
        return pivot_df
    
    def plot_Matrix_Station_vs_Hour(self, model, polutant, filename = './output/station_vs_hour'):
        '''
        Creates a matrix plot based on the df data of Stations vs Hours
        
        Parameters
        ----------
        model : string
            Column name in the dataframe df that contains the predicted values
        polutant : string
            polutant that is beiing ploted its main use is in the title\n
        filename : string, optional
            path where the plot will be save in png format
            The default is './output/station_vs_day'
            

        Returns
        -------
        pivot_df : dataframe
            table build to plot the data in case it needs to be reused o reviewed
            
        '''
        self.df['correlation'] = self.df[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]-self.df['OBSERVATION']
        pivot_df = self.df.pivot_table(values='correlation', index='NOM ESTACIO', columns='HOUR')
        plt.figure(figsize=(10,10))
        sns.set_context(font_scale=2)
        plt.title(polutant+' predicted-observed concentration \n Station vs Hour; from '+self.df['DATA'].min().strftime('%d/%m/%Y')+' to '+self.df['DATA'].max().strftime('%d/%m/%Y'))
        sns.heatmap(pivot_df, cmap='coolwarm', center=0)
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show() 
        return pivot_df    
    
    def plot_Matrix_Day_vs_Hour(self, model, polutant, filename = './output/day_vs_hour'):
        '''
        Creates a matrix plot based on the df data of Day vs Hours
        
        Parameters
        ----------
        model : string
            Column name in the dataframe df that contains the predicted values
        polutant : string
            polutant that is beiing ploted its main use is in the title            
        filename : string, optional
            path where the plot will be save in png format    
            The default is './output/station_vs_day'
            

        Returns
        -------
        pivot_df : dataframe
            table build to plot the data in case it needs to be reused o reviewed
            
        '''
        self.df['correlation'] = self.df[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']]-self.df['OBSERVATION']
        pivot_df = self.df.pivot_table(values='correlation', index='DAY', columns='HOUR')
        sns.set_context(font_scale=2)
        plt.title(polutant+' predicted-observed concentration \n Day vs Hour; from '+self.df['DATA'].min().strftime('%d/%m/%Y')+' to '+self.df['DATA'].max().strftime('%d/%m/%Y'))        
        sns.heatmap(pivot_df, cmap='coolwarm', center=0)
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show() 
        return pivot_df    




            
    def plotCorrelations(self, model, polutant, filename):
        '''
        WORK IN PROGRESS
        working on some type of grid plot with regressions analysis
        '''
        #sns.set_context('poster',font_scale=4)
        sns.lmplot(x='OBSERVATION', y=model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units'], data=self.df, col='ALTITUD', height=3)
        plt.savefig(filename, dpi=300, bbox_inches='tight')    
    

    def plotCorrelationMatrix(self, model, polutant, filename='./output/correlationMatrix'):
        '''
        WORK IN PROGRESS
        this shows a correlation matrix for different subgroups based on day and station
        It wmight be redundant with plot_Matrix_Station_vs_Day
        '''        
        
        municipis = self.df['NOM ESTACIO'].unique()
        dies = self.df['DAY'].unique()

        table = []
        for municipi in municipis:
            row = []
            for dia in dies:
                md_df = self.df[(self.df['NOM ESTACIO'] == municipi) & (self.df['DAY'] == dia)]
                cor = md_df['OBSERVATION'].corr(md_df[model+'_'+polutant+'_'+pt.AllPolutants[polutant]['obs_units']])
                row.append(cor)
            table.append(row)
            
        fig, ax = plt.subplots()
        im = ax.imshow(table)
        ax.set_xticks(np.arange(len(dies)))
        ax.set_yticks(np.arange(len(municipis)))    
        ax.set_xticklabels(np.arange(1,len(dies)+1,1), fontsize=6)
        ax.set_yticklabels(municipis,fontsize=6)
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show() 
        return table        