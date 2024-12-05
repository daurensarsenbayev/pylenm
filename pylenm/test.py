from pylenm import *
import pandas as pd

my_data_url_1 = '../content/sample_data/2018-2023.csv'
my_data_url_2 = '../content/sample_data/All_BHs.csv'

#url_1 = '../notebooks/data/FASB_Data_thru_3Q2015_Reduced_Demo.csv'
#url_2 = '../notebooks/data/FASB Well Construction Info.xlsx'

concentration_data = pd.read_csv(my_data_url_1)
construction_data = pd.read_csv(my_data_url_2)

#After importing conc data, enforce STATION_ID column as a str type, becuase pd infers types
concentration_data['STATION_ID'] = concentration_data['STATION_ID'].astype(str)

pylenm_df = PylenmDataFactory(concentration_data) # Save concentration data
pylenm_df.setConstructionData(construction_data) # Save construction data

analytes = ['Conductivity', 'Magnesium', 'Dissolved Oxygen', 'Tritium', 'Strontium-90', 'Sodium']

#pylenm_df.find_coincident_data(well_name="9054", analytes=analytes, days=100)
