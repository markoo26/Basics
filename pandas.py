##### LEGEND #####

#!# Methods/Functions that are worth using later

##### Related documentation #####
import webbrowser
webbrowser.open_new_tab("https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html")

##### Import of the libraries #####

import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6) #!# list with next 6 dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD')) #!# matrix with random values and indexes
                                                                            #!# columns defined
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'}) #!# defining different datatypes

df2.dtypes

##### Basic overview functions #####

df.head()
df.tail()
df.index
df.columns

df.to_numpy() 
df2.to_numpy() #!# Attention when used on DataFrame with different datatypes

df.describe() #!# Basic descriptive statistics 
df.T #!# Transposition of the data

df.sort_index(axis=1, ascending=False) #!# sorting by an index (sorting of the columns)
df.sort_values(by='B') #!# sorting by values

        #at, iat, loc, iloc -> recommended Pandas functions that are optimized for dataset operations

df["A"]
df[0:3]
df['20130102':'20130104']
df.loc[dates[0]] 

df.loc[:, ['A', 'B']] #!# multi-select different columns using their labels
df.loc['20130102':'20130104', ['A', 'B']]

df.loc[dates[0], 'A']
df.at[dates[0], 'A']

##### Select by position #####

df.iloc[3] #!# 4th index
df.iloc[3:5, 0:2] #!# slices
df.iloc[[1, 2, 4], [0, 2]] #!# lists

df.iloc[1, 1]
df.iat[1,1] #!# faster access

df[df.B < 0] #!# Select indexes, where column B value is lower than 0
df[df > 0] #!# Print NaNs where the condition is not met.

##### Filtering (similar to 'IN' clause from SQL) #####

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2[df2['E'].isin(['two', 'four'])] #!# searching for the two values only

##### Adding series as new column in the DataFrame #####

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

df.at[dates[0], 'A'] = 1500 #!# Set values by label
df.iat[0,1] = 2000 #!# By position
df.loc[:, 'D'] = np.array([5] * len(df)) #!# Assigning numPY array, here: repeat 5 times how many indices are available
df

df3 = df.copy()
df3[df3 > -1] = 'Low Value' #!# Equivalent to 'where' operation

##### Reindexing data #####

df1 = df.reindex(index=dates, columns=list(df.columns) + ['E'])
df1.loc[dates[1]:dates[3], 'E'] = 1

##### Missing values #####

clear_df = df1.dropna(how='any') #!# Drop them
clear_df2 = df1.fillna(value=5) #!# Fill with one value

pd.isna(df1) #!# Check missing values 
