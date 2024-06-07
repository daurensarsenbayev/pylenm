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
#pylenm_df.plot_PCA_by_date('1993-02-21', analytes)

#pylenm_df.plot_corr_by_well(well_name="FSB 95DR", analytes=analytes, remove_outliers=True, z_threshold=4, interpolate=True, frequency='2M', save_dir='plot_correlation', log_transform=False, fontsize=20, returnData=False, remove=[], no_log=None)

pylenm_df.interpose_analyte_data_by_time_proximity(well_name="9054", analytes=analytes, days=100)