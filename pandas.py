##### LEGEND #####

#!# Methods/Functions that are worth using later
##!# To revise

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

##### Basic operations #####

df.mean() #!# for columns
df.mean(1) #!# for rows
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2) #!# shift for moving series by two positions
df.sub(s, axis='index') ##!#

##### Apply functions #####

df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min()) ##!# check how to apply functions for indexes instead of columns

##### Histogramming #####
s.value_counts()

##### Merging #####

df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
df == pd.concat(pieces) #!# Check that slicing and concating gives equal results

#### Joins #####

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key') #!# All possible combinations

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pd.merge(left, right, on='key') #!# Like INNER JOIN

#### Appending data #####
s = df.iloc[3]
df.append(s, ignore_index=True) ### If False Then Index = 3 Else 10


##### Groupping #####

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

df.groupby('A').sum() #!# Groupping by one column 
df.groupby(['A', 'B']).sum() #!# Groupping by more columns

##### Stacking #####

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']])) # List with 8 two-dimensional tuples
                                                    # 1st element from 1st list with 1st element from 2nd list

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second']) ##!# Check what this function does

df5 = pd.DataFrame(np.random.randn(8, 2), 
                   index=index, 
                   columns=['A', 'B']) #!# Multi-dimensional index

stacked = df5.stack()
other = pd.DataFrame({'angles': [0, 3, 4, 5]},
                     index=['circle', 'triangle', 'rectangle', 'square'])

##### Unstack - reverse operation #####
stacked.unstack()
stacked.unstack(0)
stacked.unstack(1)


##### Pivot tables #####

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

##!# Continue from point 108

##### Multiply DataFrames #####

df * other #!# a new dataset with combination of all indexes and column is created
df6 = other
df6.mul(other, fill_value=0) #!# all NULLs are replaced with 0s

