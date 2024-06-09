
import pandas as pd
import os
import numpy as np

def interpose_analyte_data_by_time_proximity(self, days, well_name, analytes, save_dir='data/collocated/'):
    df = self.data
    df['COLLECTION_DATE'] = pd.to_datetime(df['COLLECTION_DATE'])
    query = df[df.STATION_ID == well_name]

    #The goal here is to only interpose analytes from "analytes" parameter that are present in the dataset
    #Example: analytes passed down to this function are "PH" and "Magnesium"
    #But for this well, in ANALYTE_NAME column there is not a single entry for "Magnesium", but there is "PH"
    #In that case we still want to interpose "PH" values but we do not care about "Magnesium" analyte
    a = list(np.unique(query.ANALYTE_NAME.values))
    def filter_analytes(analyte):
        return (analyte in a)
    analytes = sorted(list(filter(filter_analytes, analytes)))

    #We only perform interpositions for wells that have metrics for provided analytes
    if len(analytes) > 0:
        query = query.loc[query.ANALYTE_NAME.isin(analytes)]
        x = query[['COLLECTION_DATE', 'ANALYTE_NAME']]
        unique = ~x.duplicated()
        query = query[unique]
        piv = query.reset_index().pivot(index='COLLECTION_DATE',columns='ANALYTE_NAME', values='RESULT')
        piv = piv[analytes]
        piv.index = pd.to_datetime(piv.index)

        #Chooses a column with the least COLLECTION_DATE data points
        column_with_most_nans = None
        max_count_nans = 0
        for column in piv.columns:
            count_nans = piv[column].isna().sum()
            if count_nans > max_count_nans:
                max_count_nans = count_nans
                column_with_most_nans = column

        #We only perform interposition if there are missing data points
        if max_count_nans > 0:
            #Picks the columns where the data points are present
            df_filtered = piv.dropna(subset=[column_with_most_nans])

            #Roams the remaining columns and looks for NaN
            columns_with_nans = df_filtered.columns[df_filtered.isna().any()].tolist()
            time_window = pd.Timedelta(days=days)

            #If the RESULT for the COLLECTION_DATE is empty, the column is traversed for the closest COLLECTION_DATE data points within the provided interval
            for col in columns_with_nans:
                df_column_with_nan = self.query_data(well_name, col)

                #For every value in a column that is NaN:
                for date_index, row in df_filtered[df_filtered[col].isna()].iterrows():
                    interposition_candidates = []
                    for i, r in df_column_with_nan.iterrows():
                        date = df_column_with_nan.at[i, 'COLLECTION_DATE']
                        if (date_index + time_window >= date >= date_index - time_window):
                            interposition_candidates.append([df_column_with_nan.at[i, 'RESULT'], df_column_with_nan.at[i, 'RESULT_UNITS'], date_index])

                smallest_time_difference = pd.Timedelta(days=10000).total_seconds()
                for candidate in interposition_candidates:
                    abs_time_diff = abs((candidate[2] - date_index).total_seconds())
                    if abs_time_diff <= smallest_time_difference:
                        smallest_time_difference = abs_time_diff
                        df_filtered.at[date_index, col] = candidate[0]
                    #Addition of the interposed values to the original_df
                    new_row = { 'STATION_ID': well_name, 'ANALYTE_NAME': col, 'COLLECTION_DATE': candidate[2], 'RESULT': candidate[0], 'RESULT_UNITS': candidate[1], 'UNCERTAINTY': None }
                    df.loc[len(df)] = new_row
                smallest_time_difference = pd.Timedelta(days=10000).total_seconds()
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    df.to_csv(save_dir + 'collocation_well_' + well_name + '.csv')
    return df