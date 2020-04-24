# #!/usr/bin/env python
# # coding: utf-8
#
# # In[39]:
#
#
# import pandas as pd
# from pandas.api.types import is_numeric_dtype
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style="darkgrid")
#
#
# # In[40]:
#
# # Class needs to accept csv file
# class RegularAnalysisMethods():
#
# # This variable will be modified to be the users data set
#
#     #attributes = list()
#
#     #def set_data():
#     df = pd.read_csv('fortune500.csv')
#
#
# # This method returns a list of attributes from the dataset.
#
# # In[51]:
#
#
#     def attribute_list():
#         return list(df)
#
#
# # This is a helper method for checking attribute data types.
#
# # In[52]:
#
#
#     def check_dtype(attr_index):
#         attributes = attribute_list()
#         if is_numeric_dtype(df[attributes[attr_index]]):
#             return True
#         else:
#             return False
#
#
# # This method will output the average and standard deviation over a selected attribute, given an attribute with an appropriate data type.
#
# # In[43]:
#
#
#     def mean(attr_index):
#         attributes = attribute_list()
#         if check_dtype(attr_index):
#             mean_val = df[attributes[attr_index]].mean(skipna = True)
#             std_val = df[attributes[attr_index]].std(skipna = True)
#             return 'The calculated mean over the %s attribute is %s, with standard deviation %s.' % (attributes[attr_index], mean_val, std_val)
#         else:
#             return 'A mean value cannot be calculated due to inappropriate data type.'
#
#
# # This method will output the median over a selected attribute, given an attribute with an appropriate data type.
#
# # In[44]:
#
#
#     def median(attr_index):
#         attributes = attribute_list()
#         if check_dtype(attr_index):
#             median_val = df[attributes[attr_index]].median(skipna = True)
#             return 'The calculated median over the %s attribute is %s.' % (attributes[attr_index], median_val)
#         else:
#             return 'A median value cannot be calculated due to inappropriate data type.'
#
#
# # This method will output the mode over a selected attribute, given an attribute with an appropriate data type.
#
# # In[45]:
#
#
#     def mode(attr_index):
#         attributes = attribute_list()
#         modes = df[attributes[attr_index]].mode(dropna = True).values
#         if modes.size > 1:
#             return 'The calculated modes over the %s attribute are %s.' % (attributes[attr_index], str(modes)[1:-1])
#         else:
#             return 'The calculated mode over the %s attribute is %s.' % (attributes[attr_index], str(modes)[1:-1])
#
#
# # This method will output the min and max over a selected attribute, given an attribute with an appropriate data type.
#
# # In[46]:
#
#
#     def minmax(attr_index):
#         attributes = attribute_list()
#         if check_dtype(attr_index):
#             min_val = df[attributes[attr_index]].min(skipna = True)
#             max_val = df[attributes[attr_index]].max(skipna = True)
#             return 'The calculated minimum over the %s attribute is %s. The calculated max is %s' % (attributes[attr_index], min_val, max_val)
#         else:
#             return 'A minimum/maximum value cannot be calculated due to inappropriate data type.'
#
#
# # This method will output a general description of statistical values.
#
# # In[47]:
#
#
#     def desc_data():
#         include =['object', 'float', 'int']
#         return df.describe(include = include)
#
#
# # This will output rows within specified percentiles, given an attribute with an appropriate data type.
#
# # def perc(min, max, attr_index):
# #     if min < 1 and max < 1 and min < max:
# #         if check_dtype(attr_index):
# #             val = df[attributes[attr_index]].values
# #             q1 = np.quantile(val, q = min)
# #             q2 = np.quantile(val, q = max)
# #             mask = ((q1 < val) & (val < q2)).all(0)
# #             return df[mask]
# #         else:
# #             return 'Percentiles cannot be calculated due to inappropriate data type.'
# #     else:
# #         return 'Percentiles out of range.'
# # perc(.35,.75,0)
#
# # In[48]:
#
#
#     def interval(low_perc, high_perc, attr_index):
#         attributes = attribute_list()
#         if check_dtype(attr_index) and type(low_perc) == int and type(high_perc) == int:
#             if(low_perc < high_perc and low_perc >= 0 and high_perc <= 100):
#                 df_sort = df.sort_values(by=[attributes[attr_index]])
#                 low_bound = int(len(df)*low_perc/100)
#                 high_bound = int(len(df)*high_perc/100)
#                 return df_sort[low_bound:high_bound].copy()
#             else:
#                 print('Please enter valid percentile values.')
#         else:
#             print('Dese not numbas.')
