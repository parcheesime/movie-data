# Schema validation functions

import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema
from pathlib import Path
import yaml
import sys
import logging


# Run the schema to check column data types
def dtype_val(df):
    try:
        print(schema.validate(df, lazy=True))
    except pa.errors.SchemaErrors as err:
            print('SchemaErrors: ', err.failure_cases)


# Column name validation
def col_val(dfd):
    # clean up df columns #
    dfd.columns=dfd.columns.str.strip()
    dfd.columns=dfd.columns.str.replace(' ', '_')
    dfd.columns=dfd.columns.str.lower()
    # compare yaml columns with df columns #
    expected_columns = list(file['columns'])
    if len(dfd.columns) == len(expected_columns) and list(dfd.columns) == expected_columns:
        print('column name and column length validation passed')
        mismatched_columns_file = list(set(dfd.columns).difference(expected_columns))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_columns).difference(dfd.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df columns: {dfd.columns}')
        logging.info(f'expected columns: {expected_columns}')
        return 1
    else:
        print('column name and column length validation failed')
        mismatched_columns_file = list(set(dfd.columns).difference(expected_columns))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_columns).difference(dfd.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df columns: {dfd.columns}')
        logging.info(f'expected columns: {expected_columns}')

    return 0

# Create schema
# Create schema to keep track of columns of how I want data shaped
schema = pa.DataFrameSchema(
    {
    'popularity': Column(pa.Float64),
    'original_title': Column(pa.String), 
    'director': Column(pa.String),
    'runtime': Column(pa.Int64),
    'action': Column(pa.Int),
    'adventure': Column(pa.Int),
    'animation': Column(pa.Int),
    'comedy': Column(pa.Int),
    'crime': Column(pa.Int),
    'documentary': Column(pa.Int),
    'drama': Column(pa.Int),
    'family': Column(pa.Int),
    'fantasy': Column(pa.Int),
    'foreign': Column(pa.Int),
    'history': Column(pa.Int),
    'horror': Column(pa.Int),
    'music': Column(pa.Int),
    'mystery': Column(pa.Int),
    'romance': Column(pa.Int),
    'science_fiction': Column(pa.Int),
    'tv_movie': Column(pa.Int),
    'thriller': Column(pa.Int),
    'war': Column(pa.Int),
    'western': Column(pa.Int),
    'no_genre' : Column(pa.Int),
    'production_companies': Column(pa.String),
    'release_date': Column(pa.DateTime),
    'release_day' : Column(pa.String),
    'holiday' : Column(pa.Bool),
    'vote_count': Column(pa.Int64),
    'vote_average': Column(pa.Float64),
    'release_year': Column(pa.Int64),
    'release_year_groups' : Column(pa.Category),
    'budget_adj' : Column(pa.Float64),
    'revenue_adj' : Column(pa.Float64),
    'net_adj' : Column(pa.Float64)
}

)

# Put Schema into YAML file
yaml_sche = schema.to_yaml()
f = Path('file.yml')
f.touch()
f.write_text(yaml_sche)

with open('file.yml', 'r') as f:
    file = yaml.safe_load(f)