##### LEGEND #####

#!# Methods/Functions that are worth using later

##### Related documentation #####
import webbrowser
webbrowser.open_url("https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html")

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

=> 42