### Functions ###
import pandas as pd 

#Function to load csv file
def load_csv():
    df_main = pd.read_csv('data/world_population.csv')
    return df_main

#Function to clean columns names
def clean_columns(df_main):
    df_main.rename(columns = {'Country/Territory':'Country', '2022 Population':'Population_2022','2020 Population':'Population_2020',
                    '2015 Population':'Population_2015', '2010 Population':'Population_2010', '2000 Population':'Population_2000',
                    '1990 Population':'Population_1990', '1980 Population':'Population_1980', '1970 Population':'Population_1970', 'Area (km²)': 'Area[km2]',
                    'Density (per km²)':'Density[Km2]','Growth Rate':'Growth_Rate','World Population Percentage':'World_Population_Percentage'}, inplace=True)
    return df_main

def df_dates(df_main):
    df_dates = df_main[['Country', 'Population_2022','Population_2020','Population_2015',
            'Population_2010','Population_2000','Population_1990','Population_1980',
            'Population_1970']]
    df_dates.set_index('Country')
    df_dates = df_dates.T
    df_dates.columns = df_dates.iloc[0].set_axis(df_dates.iloc[0], axis='index')
    df_dates = df_dates.iloc[1:]
    df_dates['Year'] = ['2022', '2020','2015', '2010', '2000', '1990', '1980', '1970']
    df_dates = df_dates.set_index('Year')
    df_dates = df_dates.reset_index()
    df_dates = df_dates.sort_values(by=['Year'])
    country_list = df_dates.columns.to_list()
    country_list = country_list[1:]
    return df_dates, country_list

def country_info(df_main):
    df_info = df_main[['Rank','CCA3', 'Country', 'Capital', 'Continent','Area[km2]', 'Density[Km2]',
             'Growth_Rate', 'World_Population_Percentage' ]]
    return df_info
