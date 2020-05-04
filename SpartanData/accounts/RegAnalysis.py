import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


# This method returns a list of attributes from the dataframe.
def attribute_list(df):
    return list(df)


# This is a helper method for checking attribute data types.
def check_dtype(df, attr_index):
    attributes = attribute_list(df)
    if is_numeric_dtype(df[attributes[attr_index]]):
        return True
    else:
        return False


# This method will output the average and standard deviation
# over a selected attribute, given an attribute with an appropriate data type.
def mean(df, attr_index):
    attributes = attribute_list(df)
    if check_dtype(attr_index):
        mean_val = df[attributes[attr_index]].mean(skipna = True)
        std_val = df[attributes[attr_index]].std(skipna = True)
        return 'The calculated mean over the %s attribute is %s, with standard deviation %s.' % (attributes[attr_index], mean_val, std_val)
    else:
        return 'A mean value cannot be calculated due to inappropriate data type.'


# This method will output the median over a selected attribute,
# given an attribute with an appropriate data type.
def median(df, attr_index):
    attributes = attribute_list(df)
    if check_dtype(attr_index):
        median_val = df[attributes[attr_index]].median(skipna = True)
        return 'The calculated median over the %s attribute is %s.' % (attributes[attr_index], median_val)
    else:
        return 'A median value cannot be calculated due to inappropriate data type.'


# This method will output the mode over a selected attribute,
# given an attribute with an appropriate data type.
def mode(df, attr_index):
    attributes = attribute_list(df)
    modes = df[attributes[attr_index]].mode(dropna = True).values
    if modes.size > 1:
        return 'The calculated modes over the %s attribute are %s.' % (attributes[attr_index], str(modes)[1:-1])
    else:
        return 'The calculated mode over the %s attribute is %s.' % (attributes[attr_index], str(modes)[1:-1])

# This method will output the min and max over a selected attribute,
# given an attribute with an appropriate data type.
def minmax(df, attr_index):
    attributes = attribute_list(df)
    if check_dtype(attr_index):
        min_val = df[attributes[attr_index]].min(skipna = True)
        max_val = df[attributes[attr_index]].max(skipna = True)
        return 'The calculated minimum over the %s attribute is %s. The calculated max is %s' % (attributes[attr_index], min_val, max_val)
    else:
        return 'A minimum/maximum value cannot be calculated due to inappropriate data type.'


# This method will output a general description of statistical values.
def desc_data(df):
    include = ['object', 'float', 'int']
    return df.describe(include = include)


# This will output rows within specified percentiles, given an attribute with an appropriate data type.
def interval(df, low_perc, high_perc, attr_index):
    attributes = attribute_list(df)
    if check_dtype(attr_index) and type(low_perc) == int and type(high_perc) == int:
        if(low_perc < high_perc and low_perc >= 0 and high_perc <= 100):
            df_sort = df.sort_values(by=[attributes[attr_index]])
            low_bound = int(len(df)*low_perc/100)
            high_bound = int(len(df)*high_perc/100)
            return df_sort[low_bound:high_bound].copy()
        else:
            print('Please enter valid percentile values.')
            return null
    else:
        print('Dese not numbas.')
        return null


# This method takes in x and y attribute indices and creates a json file to be used in a line plot.
def line_plot(df, x_index, y_index):
    df1 = df.iloc[:,[x_index, y_index]]
    df1['tuple']=list(zip(df.iloc[:,x_index],df.iloc[:,y_index]))
    df1['tuple'].to_json('line_plot.json',orient='values')


# This method takes an attribute index and creates a json file to be used in a histogram.
def histogram(df, x_index):
    df1 = df.iloc[:,x_index].value_counts().reset_index()
    df1['tuple']=list(zip(df1.iloc[:,1],df1.iloc[:,0]))
    df1['tuple'].to_json('histogram.json',orient='values')


# This method takes an attribute index and creates a json file to be used in a donut chart.
def donut_chart(df, x_index):
    df1 = df.iloc[:,x_index].value_counts().reset_index()
    total = df1.iloc[:,1].sum()/100
    df1['tuple']=list(zip(df1.iloc[:,1]/total,df1.iloc[:,0]))
    df1['tuple'].to_json('donut_chart.json',orient='values')

