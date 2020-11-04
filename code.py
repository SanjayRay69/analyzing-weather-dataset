# --------------
import pandas as pd
import numpy as np
from scipy.stats import mode 
weather = pd.read_csv(path)
def categorical(df):
    categorical_var = df.select_dtypes(include = 'object')
    return categorical_var.columns
categorical(weather)
def numerical(df):
    numerical_var = df.select_dtypes(include = 'number')
    return numerical_var.columns
numerical(weather)
def clear(df, col, val):
    return df[df[col] == val].count()
clear(weather, 'Weather', 'Cloudy')
def instances_based_condition(df, col1, val1, col2, val2):
    x = df[(df[col1] > val1) & (df[col2] == val2)]
    return x
wind_speed_35_vis_25 = instances_based_condition(weather, 'Wind Spd (km/h)', 35, 'Visibility (km)', 25)
weather['month'] = pd.DatetimeIndex(weather['Date/Time']).month
def agg_values_ina_month(df):
    y = pd.pivot_table(weather,index='month', values='Temp (C)',aggfunc=['mean', 'max', 'min', 'sum'])
    return (y)
agg_values_ina_month(weather)
def group_values(df):
    x = df.groupby('Weather').agg({'Temp (C)':'mean', 'Dew Point Temp (C)':'mean', 'Rel Hum (%)':'mean', 'Wind Spd (km/h)':'mean', 'Visibility (km)':'mean', 'Stn Press (kPa)':'mean'})
    return x
mean_weather = group_values(weather)
cols = ['Temp (C)', 'Dew Point Temp (C)']
new_cols = []
for str in cols:
    new_col = str.replace('C', 'F')
    new_cols.append(new_col)
       
def convert(df, new_cols):
    df[new_cols] = df[cols] * 1.8 + 32
    print('Temperatures in fahrenheit are:')
    return df[new_cols] 
convert(weather, new_cols)




