import pandas as pd
from pandas.core.common import flatten

# Functions to clean up categories
# make type string

# Faster replace
def replace_pipe(df, col_name):
    replaced=df[col_name].str.replace('\|', ',', regex=True)
    return replaced


# Separate the string and get a unique list of categories
def get_unique_list(df, col_name):
    new_list=list(df[col_name].unique())
    new_list=[str(elems).split(',') for elems in new_list]
    new_list=list(flatten(new_list))
    new_list=set(new_list)
    return new_list


# add new genre columns to mdf, set all values to zero
def insert_zero(df, col_names):
    for c in col_names:
        df[c]=0
    return df


 # function to change new column value to 1 if category is present in old column. 
def category_present(df, og_column_name, unique_category):
    for k, v in df[og_column_name].iteritems():
        x=str(v).split(',')
        for i in x:
            if i==unique_category:
                df.loc[k, unique_category]=1
    return df[unique_category].unique()   