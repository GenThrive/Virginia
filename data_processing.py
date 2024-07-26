# Libraries
# Data
import math
import numpy as np
import pandas as pd # Dataframe manipulations
import geopandas as gpd

# ----------------------------------------------------------------------------
# DATA LOADING AND CLEANING FUNCTIONS
# ----------------------------------------------------------------------------


def multiterm_columns(columns_dictionary, table_name):
    to_explode = columns_dictionary.loc[
        (columns_dictionary['table_name'] == table_name)
        & (columns_dictionary['multiple_values'] == "Yes"),
        'column_name'
    ].unique()
    return list(to_explode)


def get_display_terms(controlled_terms_df, table, column):
    """
    Produce dataframe with: term, display_term

    :param controlled_terms_df:
    :param table:
    :param column:
    :return:
    """
    controlled_terms_df = controlled_terms_df[controlled_terms_df['table_name'] == table]
    controlled_terms_df = controlled_terms_df[controlled_terms_df['column_name'] == column]
    controlled_terms_df = controlled_terms_df.loc[:, ['term', 'display_term']]
    controlled_terms_df = controlled_terms_df.set_index('term')
    return controlled_terms_df

def strip_x(x):
    if x:
        return x.strip()

def program_count_by_metric(df,id_col,metric_col ):
    """
    Get a count of all entries that contain values from a particular metric column.
    **Input column as an array**

    If metric column dtype is a string, turn it into a list, then explode, group and count.
    """
    metric_df = df[[id_col, metric_col]].copy() # get subset of df as a copy
    metric_df = metric_df.explode(metric_col) # explode to give each element of list its own row
    metric_df[metric_col] = metric_df[metric_col].apply(lambda x: strip_x(x)) # strip whitespaces from entries
    metric_df = metric_df.replace(r'^\s*$', 'Unspecified', regex=True)
    metric_df = metric_df.replace(np.nan, 'Unspecified')
    metric_df = metric_df.groupby(metric_col).count() # count the number of rows for each entry
    metric_df.columns = ['Count']    # rename from id_col to count
    metric_df.reset_index(inplace=True) # turn metric col from index back into col so dataframe structured for data viz
    return metric_df


def merge_with_controlled_terms(df, controlled_terms_df, table_name, column_name):
    ''' Merge a dataframe with display terms from the dictionary'''
    display_terms = controlled_terms_df[(controlled_terms_df['table_name']==table_name)&(controlled_terms_df['column_name']==column_name)][['term','display_term']]
    display_terms_col_name = controlled_terms_df[(controlled_terms_df['table_name']==table_name)&(controlled_terms_df['column_name']==column_name)]['display_name'].unique()
    display_terms.columns = ['term', display_terms_col_name[0]]

    # add a lower case column to both dataframes to merge on to correct for capitalization issues
    df['merge'] = df[column_name].str.lower().apply(lambda x: strip_x(x)) # strip whitespaces from entries
    display_terms['merge'] = display_terms['term'].str.lower().apply(lambda x: strip_x(x)) # strip whitespaces from entries
    merged_df = pd.merge(df, display_terms, how='left', on='merge')

    # Drop merge column and fill NaN with 'No Data'
    merged_df = merged_df.drop(columns=['merge'])
    # merged_df = merged_df.fillna('No Data Entered')

    return merged_df


def get_chart_data(df,id_col,metric_col, controlled_terms_df, table_name, column_name=None):
    ''' get chart_data.  default column_name as None, in which case column_name = metric_col'''
    if column_name == None:
        column_name = metric_col
    chart_data = program_count_by_metric(df, id_col, metric_col)
    chart_data = merge_with_controlled_terms(chart_data, controlled_terms_df, table_name, column_name)
    return chart_data

def explode_multiple(df, explode_cols):
    new_df = df.copy()
    for col in explode_cols:
        new_df = new_df.explode(col)
    return new_df
