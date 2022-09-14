# Movies Dataset Investigation
### Purpose

Conduct data analysis on movie dataset and create a file to share that documents your findings on Udacity classroom, unit 2 Project: Investigate a Dataset.

### Introduction

This movie dataset was supplied by Udacity, called IMDb movie data:

[IMDb movie data](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/July/5b57919a_data-set-options/data-set-options.pdf)

RangeIndex: 10866 entries, 0 to 10865

Data columns (total 21 columns):
 #   Column                Non-Null Count  Dtype 

---  ------                --------------  -----  

 0   id                    10866 non-null  int64  

 1   imdb_id               10856 non-null  object 

 2   popularity            10866 non-null  float64

 3   budget                10866 non-null  int64  

 4   revenue               10866 non-null  int64  

 5   original_title        10866 non-null  object 

 6   cast                  10790 non-null  object 

 7   homepage              2936 non-null   object 

 8   director              10822 non-null  object 

 9   tagline               8042 non-null   object 

 10  keywords              9373 non-null   object 

 11  overview              10862 non-null  object 

 12  runtime               10866 non-null  int64  

 13  genres                10843 non-null  object 

 14  production_companies  9836 non-null   object 

 15  release_date          10866 non-null  object 

 16  vote_count            10866 non-null  int64  

 17  vote_average          10866 non-null  float64

 18  release_year          10866 non-null  int64  

 19  budget_adj            10866 non-null  float64

 20  revenue_adj           10866 non-null  float64

dtypes: float64(4), int64(6), object(11)

### Process
This project uses Pandas, NumPy, Matplotlib, and other libraries to wrangle, explore, analyze and communicate data.

- 3 separate jupyter notebook files
- 3 spearate .py files for functions used in the ipynb files

### Acknowledgments

- Stackoverflow
- Udacity lessons
- Data Validation Project
- GitHub pandera