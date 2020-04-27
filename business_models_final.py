# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:41:52 2020

@author: Mike
"""
#Data Science Capstone
#Michael Bassett

#This is the fourth set of code used for the "business.json" yelp dataset
#After the business_pre_SAS.py file, the SAS data cleaning file, and business_feature_selection.py

#Business Models - Final Python File

import pandas as pd
import numpy as np
from numpy import set_printoptions
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

set_printoptions(precision=4)
np.set_printoptions(suppress=True)

#Read in the dataset that we cleaned in SAS
FD = pd.read_csv('SAS/FD_SAS.csv')
print(len(FD))
#29558

#Create an overall labels dataset
labels = np.array(FD['STARS2'])
print(labels.shape)
#29558

#Creating each city subset and verifying that the length is correct
#Also creating the labels for each city

calgary = FD[FD["state"] == 'AB']
calgary_labels = np.array(calgary['STARS2'])
print(calgary_labels.shape)
#2914

toronto = FD[FD["state"] == 'ON']
toronto_labels = np.array(toronto['STARS2'])
print(toronto_labels.shape)
#7965

pittsburgh = FD[FD["state"] == 'PA']
pittsburgh_labels = np.array(pittsburgh['STARS2'])
print(pittsburgh_labels.shape)
#2455

charlotte = FD[FD["state"] == 'NC']
charlotte_labels = np.array(charlotte['STARS2'])
print(charlotte_labels.shape)
#2710

phoenix = FD[FD["state"] == 'AZ']
phoenix_labels = np.array(phoenix['STARS2'])
print(phoenix_labels.shape)
#4000

lasvegas = FD[FD["state"] == 'NV']
lasvegas_labels = np.array(lasvegas['STARS2'])
print(lasvegas_labels.shape)
#6811

madison = FD[FD["state"] == 'WI']
madison_labels = np.array(madison['STARS2'])
print(madison_labels.shape)
#1128

cleveland = FD[FD["state"] == 'OH']
cleveland_labels = np.array(cleveland['STARS2'])
print(cleveland_labels.shape)
#1575

#All of the counts are what we expect

#Beginning of the Model Portion

#NOTE - THE BELOW CODE WAS RUN REPEATEDLY FOR ALL 8 CITIES, FOR BOTH STARS1 AND STARS2
#THE FEATURES WERE CHANGED BASED ON WHATEVER FEATURES WERE MOST IMPORTANT FOR THAT CITY
#THE RESULTS WERE THEN INCLUDED IN THE EXCEL FILE

#Here you will enter in the top features based on Feature Selection results

features = cleveland.loc[:,['review_count','NOISELEVEL2','VALIDATED2',
'BURGERS', 'CATERS2', 'DELIVERY2', 'GARAGE2', 'GOODFORKIDS2', 'LOT2', 'pricerange', 'TOURISTY2', 'VALET2', 'WIFI2'

]]

#Convert selected features into a numpy array
features = np.array(features)
print(type(features))

#Split the data up into train and test subsets
x_train, x_test, y_train, y_test = train_test_split(features,cleveland_labels,test_size=0.20,random_state=0)

#Look at the shape to make sure that it makes sense
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

#MODEL 1 - RANDOM FOREST CLASSIFIER

rf = RandomForestClassifier(n_estimators = 100, random_state = 0)
rf.fit(x_train, y_train)
round(rf.score(x_test,y_test), 4)

#MODEL 2 - LOGISTIC REGRESSION - STARS1
LR1 = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(x_train, y_train)
round(LR1.score(x_test,y_test), 4)

#MODEL 3 - LOGISTIC REGRESSION - STARS2

LR2 = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x_train, y_train)
round(LR2.score(x_test,y_test), 4)




