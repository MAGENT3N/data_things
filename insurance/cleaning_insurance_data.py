# -*- coding: utf-8 -*-
"""
   Program for cleaning the data
"""
import pandas as pd

#%%

# Loading the data as as dataframe

df = pd.read_csv("insurance.csv")
#%%
df.info()


#%%
""" 
   CLEANING THE DATA-
   1)checking for rogue values like something etc
    ... and matching their type
   
    2)Transforming the column data in a uniform form
    
    3)Either the drop the rows with nan values or fill
    ...them, I chose to fill them. Fill each column de
    epeniding upon the metric like what is good,mean ?
    median ? mode?{mode is good for objects} or a custom
    procedure the we can create
    
    4)Fill the nan values with your guesses
"""
#%%

# Converting all the entries in sex column to lower case
#... then looking at the firs letter if 'm' then value = 0
#... and if 'f' then values = 1
df['sex'] = df['sex'].str.lower().str[0].map({'m':0 ,'f':1})
#%%
# Converting all the smoker data to binaries?
df['smoker'] = df['smoker'].str.lower().str[0].map({'y':1,'n':0})
#%%
# Converting charges to float by removing dollar and string to float
df['charges'] = df['charges'].str.lstrip('$')
# Converting to float
df['charges'] = pd.to_numeric(df['charges'],errors = 'coerce')
#%%
# Fill nan values in the charges column to the median?
#... well median is file since we dont want outliers to
#...effect our analysis
df['charges'] = df['charges'].fillna(df['charges'].median())
# Fill nan values in sex with modal value
df['sex'] = df['sex'].fillna(df['sex'].mode()[0])
#%%
# cleaning the ages column and fill nan with modal age
df['age'] = df['age'].abs()
# filling with mean age
df['age'] = df['age'].fillna(df['age'].mode()[0])
# cleaning bmi and filling nan with mean bmi 
df['bmi'] = df['bmi'].fillna(df['bmi'].mean())
# cleaning ages by first getting abs values since 
#..some are negative and the filling with modal value
df['children'] = df['children'].abs()
df['children'] = df['children'].fillna(df['children'].mode()[0])
# same with smokers
df['smoker'] = df['smoker'].fillna(df['smoker'].mode()[0])
#%%
#Setting the region column to lower case then filling
#..nan values to the most frequent region
df['region'] = df['region'].str.lower()
df['region'] = df['region'].fillna(df['region'].mode()[0])
#%%
#download the cleaned csv
df.to_csv('cleaned_insurance.csv', index = False)