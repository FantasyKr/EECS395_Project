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
def data_prep(df):
    df = df.fillna(value=0)
    replace_values = {'negative':0, 'positive':1, 'f':0, 't':1}
    df = df.replace(to_replace=replace_values)
    return df
#test method
def methodA(value):
    some_variable = value
    return some_variable
# This method returns a list of attributes from the dataframe.
def attribute_list(df):
    return list(df)

# Example code for running a model:
# df = pd.read_csv('Jan_2019_ontime.csv', skip_blank_lines = True)
# df = data_prep(df)
# feature_list = [0,1,6,13,14,18]

# An array is returned with the numeric metrics and a file 
# 'confusion_matrix.png' holding the confusion matrix is saved.

# This method receives a dataframe, the index of the attribute
# we are predicting, and a list of indices of features we want
# to train the model on. These indices are based off of the list
# produced by attribute_list(). A random forest model is then used 
# to train and label the data. The method returns two metric values
# (accuracy and ROC AUC score) and a confusion matrix in a png file.
def rand_forest(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = RandomForestClassifier()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)

    a_string = "Accuracy (in percentage) of Random Forest Model: "
    accuracy = str(accuracy_score(y_test,y_predicted)*100)
    r_string = "ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label): "
    ROC = str(roc_auc_score(y_test,y_predicted))

    # Plot normalized confusion matrix
    disp = plot_confusion_matrix(classifier, X_test, y_test, 
                                 cmap=plt.cm.Blues,normalize='true').ax_.set_title("Normalized confusion matrix")
    plt.savefig('confusion_matrix.png')
    return [a_string + accuracy, r_string + ROC]


# This method receives a dataframe, the index of the attribute
# we are predicting, and a list of indices of features we want
# to train the model on. These indices are based off of the list
# produced by attribute_list(). A K Nearest Neighbors clustering
# model is then used to train and label the data. The method returns
# two metric values (accuracy and ROC AUC score) and a confusion matrix in a png file.
def k_neighbors(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = KNeighborsClassifier()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)
    
    a_string = "Accuracy (in percentage) of K Nearest Neighbors Model: "
    accuracy = str(accuracy_score(y_test,y_predicted)*100)
    r_string = "ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label): "
    ROC = str(roc_auc_score(y_test,y_predicted))

    # Plot normalized confusion matrix
    disp = plot_confusion_matrix(classifier, X_test, y_test, 
                                 cmap=plt.cm.Blues,normalize='true').ax_.set_title("Normalized confusion matrix")
    plt.savefig('confusion_matrix.png')
    return [a_string + accuracy, r_string + ROC]


# This method receives a dataframe, the index of the attribute
# we are predicting, and a list of indices of features we want
# to train the model on. These indices are based off of the list
# produced by attribute_list(). A Gaussian Naive Bayes model is
# then used to train and label the data. The method returns two 
# metric values (accuracy and ROC AUC score) and a confusion matrix in a png file.
def naive_bayes(df, pred_attr_index, feature_list):
    X = df.iloc[:,feature_list]
    y = df.iloc[:,pred_attr_index]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)
    model = GaussianNB()
    classifier = model.fit(X_train,y_train)
    y_predicted = model.predict(X_test)
    
    a_string = "Accuracy (in percentage) of Gaussian Naive Bayes Model: "
    accuracy = str(accuracy_score(y_test,y_predicted)*100)
    r_string = "ROC AUC score (this metric measures the probability that a correct label is preferred over an incorrect label): "
    ROC = str(roc_auc_score(y_test,y_predicted))

    # Plot normalized confusion matrix
    disp = plot_confusion_matrix(classifier, X_test, y_test, 
                                 cmap=plt.cm.Blues,normalize='true').ax_.set_title("Normalized confusion matrix")
    plt.savefig('confusion_matrix.png')
    return [a_string + accuracy, r_string + ROC]
