#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
import itertools
sns.set(style="darkgrid")


# This prep method should be run on a dataset before any model.

# In[ ]:


def data_prep(df):
    df = df.fillna(value=0)
    replace_values = {'negative':0, 'positive':1, 'f':0, 't':1}
    df = df.replace(to_replace=replace_values)
    return df


# This method returns a list of attributes from the dataframe.

# In[ ]:


def attribute_list(df):
    return list(df)


# In[ ]:


# Example code for running a model:

# df = pd.read_csv('Jan_2019_ontime.csv', skip_blank_lines = True)
# df = data_prep(df)
# feature_list = [0,1,6,13,14,18]
# rand_forest(df, 17, feature_list)


# This method receives a dataframe, the index of the attribute we are predicting, and a list of indices of features we want to train the model on. These indices are based off of the list produced by attribute_list(). A random forest model is then used to train and label the data. The method returns two metric values (accuracy and ROC AUC score) and a confusion matrix.

# In[ ]:


def rand_forest(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = RandomForestClassifier()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)

    print("Accuracy (in percentage) of Random Forest Model:")
    print(accuracy_score(y_test,y_predicted)*100)
    print("ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label):")
    print(roc_auc_score(y_test,y_predicted))

    # Plot normalized confusion matrix
    titles_options = [("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(classifier, X_test, y_test,
                                     cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)
        print(title)


# This method receives a dataframe, the index of the attribute we are predicting, and a list of indices of features we want to train the model on. These indices are based off of the list produced by attribute_list(). A K Nearest Neighbors clustering model is then used to train and label the data. The method returns two metric values (accuracy and ROC AUC score) and a confusion matrix.

# In[ ]:


def k_neighbors(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = KNeighborsClassifier()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)
    
    print("Accuracy (in percentage) of K Nearest Neighbors Model")
    print(accuracy_score(y_test,y_predicted)*100)
    print("ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label):")
    print(roc_auc_score(y_test,y_predicted))

    
    # Plot normalized confusion matrix
    titles_options = [("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(classifier, X_test, y_test,
                                     cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)
        print(title)


# This method receives a dataframe, the index of the attribute we are predicting, and a list of indices of features we want to train the model on. These indices are based off of the list produced by attribute_list(). A Gaussian Naive Bayes model is then used to train and label the data. The method returns two metric values (accuracy and ROC AUC score) and a confusion matrix.

# In[ ]:


def naive_bayes(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = GaussianNB()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)
    
    print("Accuracy (in percentage) of Gaussian Naive Bayes Model")
    print(accuracy_score(y_test,y_predicted)*100)
    print("ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label):")
    print(roc_auc_score(y_test,y_predicted))

    # Plot normalized confusion matrix
    titles_options = [("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(classifier, X_test, y_test,
                                     cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)
        print(title)

