import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('out.csv')

# Function to find the max number of movies released per genre and 5 year grouping
def max_genre_by_year(genre):
    action_yr=df.groupby('release_year_groups')[genre].sum()
    year=action_yr.idxmax()
    max=action_yr.max()
    return [genre, max, year]

    # For each genre, create a function to find the year groups that it was the most popular 
    # and it's popularity score, ( then find most popular genre for each year)
def popular_genre_by_year(df, genre):
    df=df.loc[df[genre]==1]
    max_popularity_group=df.groupby('release_year_groups')['popularity'].max()
    max_popularity=max_popularity_group.max()
    max_id=max_popularity_group.idxmax()
    return [genre, max_id, max_popularity]

    # Function to group by numerical column according to specified year grouping and dataframe
def rel_yr_grps(df, year_group, num_col):
    df=df.loc[df['release_year_groups']==year_group]
    num_col_max=df.loc[df[num_col].idxmax()]
    num_col_max=num_col_max.to_frame().reset_index()
    num_col_max=num_col_max.rename(columns={num_col_max.columns[1]: 'max_info'})
    return [year_group, num_col_max['max_info'][4], num_col_max['max_info'][13]]

