"""
   Program for working with cleaned data
"""
#
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%
#Loading the cleaned data as a data_frame

cleaned_df = pd.read_csv('cleaned_insurance.csv')


#%%
#Function for plotting scatter plots takes in the 
#... x argument y_argument and the title(in vs form)
def plot_scatter(x_arg,y_arg,title):
    plt.figure()
    plt.scatter(x_arg , y_arg)
    plt.title(f'{title} vs charges')
    plt.show()
#%%    
# Try building scatter plots between the different
#..features to get an idea of a relationship with the independent
#..the function we are trying to predict(charges in this case)
for columns in cleaned_df.columns:
    plot_scatter(cleaned_df[columns],cleaned_df['charges'],columns)

#>-- Results - No extremely non-linear relationships 
#... being a smoker has a positive correlation with charges so we
#... can apply regression
#%% Preparing the data for model fitting main problem
# ... is the regions column main,use hot encoding
# dtype=int for converting true and false to 1 and 0
cleaned_df = pd.get_dummies(cleaned_df,columns =['region'],dtype=int)
#%% Fitting the data to an OLS linear model using scikitlearn


#Input = every variable except charges
#... output = charges

X = cleaned_df.drop(columns = ['charges'])
y = cleaned_df['charges']

#splitting the data into training and testing
X_train,X_test,y_train,y_test = train_test_split(X , y , test_size=0.2,random_state=42)

# Creating the model
model =RandomForestRegressor(random_state=42)
model.fit(X_train,y_train)

# Checking outputs based on the models on the X_testing data
y_predictions = model.predict(X_test)

# Calculating the r**2 error for evauluating performance
r_squared = r2_score(y_test , y_predictions)
print(r_squared)
#%%





