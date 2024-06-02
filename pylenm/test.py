from pylenm import *
import pandas as pd

url_1 = '../notebooks/data/FASB_Data_thru_3Q2015_Reduced_Demo.csv'
url_2 = '../notebooks/data/FASB Well Construction Info.xlsx'

concentration_data = pd.read_csv(url_1)
construction_data = pd.read_excel(url_2)

#After importing conc data, enforce STATION_ID column as a str type, becuase pd infers types
concentration_data['STATION_ID'] = concentration_data['STATION_ID'].astype(str)

pylenm_df = PylenmDataFactory(concentration_data) # Save concentration data
pylenm_df.setConstructionData(construction_data) # Save construction data

# analytes = ['TRITIUM','SPECIFIC CONDUCTANCE', 'PH','URANIUM-238', 'DEPTH_TO_WATER']

# PyLenm functions to test

pylenm_df.plot_all_time_series_simple(start_date='2015-1-8', min_days=100, save_dir='data/')

# Fixed


# class PylenmDataFactory(object):
# __isValid_Data
# __set_units()
# __REQUIREMENTS_DATA
# def __isValid_Data(self, data):
# __hasColumns_Data
# def __set_units(self):
# def __isValid_Construction_Data(self, data):
# def __hasColumns_Data(self, data): 
# def __hasColumns_Construction_Data(self, data):
# def setConstructionData(self, construction_data: pd.DataFrame, verbose=True):
# def jointData_is_set(self, lag):
# def __set_jointData(self, data, lag):
# def getData(self):
# def get_Construction_Data(self):
# def __REQUIREMENTS_DATA(self):
# def __REQUIREMENTS_CONSTRUCTION_DATA(self):
# def __custom_analyte_sort(self, analytes):
# def __plotUpperHalf(self, *args, **kwargs):
# def simplify_data(self, data=None, inplace=False, columns=None, save_csv=False, file_name= 'data_simplified', save_dir='data/'):
# def get_MCL(self, analyte_name):
# def get_unit(self, analyte_name):
# def filter_by_column(self, data=None, col=None, equals=[]):
# def filter_wells(self, units):
# def remove_outliers(self, data, z_threshold=4):
# def get_analyte_details(self, analyte_name, filter=False, col=None, equals=[], save_to_file = False, save_dir='analyte_details'):
# def get_data_summary(self, analytes=None, sort_by='date', ascending=False, filter=False, col=None, equals=[]):
# def get_well_analytes(self, well_name=None, filter=False, col=None, equals=[]):
# def query_data(self, well_name, analyte_name):
#   def plot_data(self, well_name, analyte_name, log_transform=True, alpha=0,
#   def plot_all_data(self, log_transform=True, alpha=0, year_interval=2, plot_inline=True, save_dir='plot_data'):
# def plot_correlation_heatmap(self, well_name, show_symmetry=True, color=True, save_dir='plot_correlation_heatmap'):
#   def plot_all_correlation_heatmap(self, show_symmetry=True, color=True, save_dir='plot_correlation_heatmap'):
# def interpolate_well_data(self, well_name, analytes, frequency='2W'):
# Correlations
#     def plot_corr_by_well(self, well_name, analytes, remove_outliers=True, z_threshold=4, interpolate=False, frequency='2W', save_dir='plot_correlation', log_transform=False, fontsize=20, returnData=False, remove=[], no_log=None):

#   def plot_all_corr_by_well(self, analytes, remove_outliers=True, z_threshold=4, interpolate=False, frequency='2W', save_dir='plot_correlation', log_transform=False, fontsize=20):

# def plot_corr_by_date_range(self, date, analytes, lag=0, min_samples=10, save_dir='plot_corr_by_date', log_transform=False, fontsize=20, returnData=False, no_log=None):

#   def plot_corr_by_year(self, year, analytes, remove_outliers=True, z_threshold=4, min_samples=10, save_dir='plot_corr_by_year', log_transform=False, fontsize=20, returnData=False, no_log=None):
# Added 
# def plot_corr_by_well(self, well_name, analytes, remove_outliers=True, z_threshold=4, interpolate=False, frequency='2W', save_dir='plot_correlation', log_transform=False, fontsize=20, returnData=False, remove=[], no_log=None):
# Method = c(‘interpolate’, ‘colocate’) 
# Window = ‘2W’ 

#   def plot_MCL(self, well_name, analyte_name, year_interval=5, save_dir='plot_MCL'):
#     def plot_PCA_by_date(self, date, analytes, lag=0, n_clusters=4, return_clusters=False, min_samples=3, show_labels=True, save_dir='plot_PCA_by_date', filter=False, col=None, equals=[]):
#   def plot_PCA_by_year(self, year, analytes, n_clusters=4, return_clusters=False, min_samples=10, show_labels=True, save_dir='plot_PCA_by_year', filter=False, col=None, equals=[]):
#   def plot_PCA_by_well(self, well_name, analytes, interpolate=False, frequency='2W', min_samples=10, show_labels=True, save_dir='plot_PCA_by_well'):
#   def plot_coordinates_to_map(self, gps_data, center=[33.271459, -81.675873], zoom=14) -> Map:
#     def interpolate_wells_by_analyte(self, analyte, frequency='2W', rm_outliers=True, z_threshold=3):
#   def __transform_time_series(self, analytes=[], resample='2W', rm_outliers=False, z_threshold=4):
#   def __get_individual_analyte_df(self, data, dates, analyte):
#     def __cluster_data_OLD(self, data, n_clusters=4, log_transform=False, filter=False, filter_well_by=['D'], return_clusters=False):
#   def cluster_data(self, data, analyte_name=["ANALYTE_NAME"], n_clusters=4, filter=False, col=None, equals=[], year_interval=5, y_label = 'Concentration', return_clusters=False ):
#     def plot_all_time_series_simple(self, analyte_name=None, start_date=None, end_date=None, title='Dataset: Time ranges', x_label='Well', y_label='Year',x_label_size=8, min_days=10, x_min_lim=-5, x_max_lim = 170, y_min_date='1988-01-01', y_max_date='2020-01-01', return_data=False, filter=False, col=None, equals=[]): 
#   def plot_all_time_series(self, analyte_name=None, title='Dataset: Time ranges', x_label='Well', y_label='Year', x_label_size=8, marker_size=30  min_days=10, x_min_lim=None, x_max_lim=None, y_min_date=None, y_max_date=None, sort_by_distance=True, source_coordinate=[436642.70,3681927.09], log_transform=False, cmap=mpl.cm.rainbow,   drop_cols=[], return_data=False, filter=False, col=None, equals=[], cbar_min=None, cbar_max=None, reverse_y_axis=False, fontsize = 20, figsize=(20,6), dpi=300, y_2nd_label=None):
# def plot_all_time_series(self, analyte_name=None, title='Dataset: Time ranges', x_label='Well', y_label='Year', x_label_size=8, marker_size=30, min_days=10, x_min_lim=None, x_max_lim=None, y_min_date=None, y_max_date=None, sort_by_distance=True, source_coordinate=[436642.70,3681927.09], log_transform=False, cmap=mpl.cm.rainbow, drop_cols=[], return_data=False, filter=False, col=None, equals=[], cbar_min=None, cbar_max=None, reverse_y_axis=False, fontsize = 20, figsize=(20,6), dpi=300, y_2nd_label=None):
# def __getLagDate(self, date, lagDays=7):
#     def getCleanData(self, analytes):   
# def getCommonDates(self, analytes, lag=[3,7,10]):
# getJointData(self, analytes, lag=3):
# def mse(self, y_true, y_pred):
# def get_Best_GP(self, X, y, smooth=True, seed = 42):
# def fit_gp(self, X, y, xx, model=None, smooth=True):
# def interpolate_topo(self, X, y, xx, ft=['Elevation'], model=None, smooth=True, regression='linear', seed = 42):
#   def __get_Best_Well(self, X, y, xx, ref, selected, leftover, ft=['Elevation'], regression='linear', verbose=True, smooth=True, model=None):
#   def get_Best_Wells(self, X, y, xx, ref, initial, max_wells, ft=['Elevation'], regression='linear', verbose=True, smooth=True, model=None):
#   def dist(self, p1, p2):
# def add_dist_to_source(self, XX, source_coordinate=[436642.70,3681927.09], col_name='dist_to_source'):

