# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:23:20 2020

@author: Mike
"""
#Data Science Capstone
#Michael Bassett

#This is the third set of code used for the "business.json" yelp dataset
#After the business_pre_SAS.py file and the SAS data cleaning file

#Feature Selection

import pandas as pd
import numpy as np
from numpy import set_printoptions
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.ensemble import ExtraTreesClassifier

#Print options which are adjusted based on each feature selection method
set_printoptions(precision=0)
np.set_printoptions(suppress=True)

#This is our clean dataframe with all 8 cities, pulled from SAS
FD = pd.read_csv('SAS/FD_SAS.csv')
print(len(FD))
#29558

#Creating each city subset and verifying that the length is correct

calgary = FD[FD["state"] == 'AB']
print(len(calgary))
#2914

toronto = FD[FD["state"] == 'ON']
print(len(toronto))
#7965

pittsburgh = FD[FD["state"] == 'PA']
print(len(pittsburgh))
#2455

charlotte = FD[FD["state"] == 'NC']
print(len(charlotte))
#2710

phoenix = FD[FD["state"] == 'AZ']
print(len(phoenix))
#4000

lasvegas = FD[FD["state"] == 'NV']
print(len(lasvegas))
#6811

madison = FD[FD["state"] == 'WI']
print(len(madison))
#1128

cleveland = FD[FD["state"] == 'OH']
print(len(cleveland))
#1575

#The counts are correct

#Now creating the feature and label subsets for each of the 8 cities

f = FD.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
f = np.array(f)
l = np.array(FD['STARS2'])
#print(type(f))
#print(type(l))
print(f.shape)
print(l.shape)

calgary_f = calgary.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
calgary_f = np.array(calgary_f)
calgary_l = np.array(calgary['STARS2'])

toronto_f = toronto.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
toronto_f = np.array(toronto_f)
toronto_l = np.array(toronto['STARS2'])

pittsburgh_f = pittsburgh.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
pittsburgh_f = np.array(pittsburgh_f)
pittsburgh_l = np.array(pittsburgh['STARS2'])

charlotte_f = charlotte.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
charlotte_f = np.array(charlotte_f)
charlotte_l = np.array(charlotte['STARS2'])

phoenix_f = phoenix.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
phoenix_f = np.array(phoenix_f)
phoenix_l = np.array(phoenix['STARS2'])

lasvegas_f = lasvegas.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
lasvegas_f = np.array(lasvegas_f)
lasvegas_l = np.array(lasvegas['STARS2'])

madison_f = madison.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
madison_f = np.array(madison_f)
madison_l = np.array(madison['STARS2'])

cleveland_f = cleveland.drop(['business_id'],axis=1).drop(['categories'],axis=1).drop(['latitude'],axis=1).drop(['longitude'],axis=1).drop(['postal_code'],axis=1).drop(['stars'],axis=1).drop(['state'],axis=1).drop(['CITY2'],axis=1).drop(['STARS1'],axis=1).drop(['STARS2'],axis=1)
cleveland_f = np.array(cleveland_f)
cleveland_l = np.array(cleveland['STARS2'])

#Now we can begin the Feature Selection Portion

#NOTE - THE BELOW CODE WAS RUN REPEATEDLY FOR ALL 8 CITIES, FOR BOTH STARS1 AND STARS2

#Model 1 - Recursive Feature Elimination with Random Forest Classifier

#Top 8
model1 = RandomForestClassifier(n_estimators = 100, random_state = 0)
rfe = RFE(model1, 8)
fit = rfe.fit(cleveland_f, cleveland_l)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

#Model 2A - Recursive Feature Elimination with Logistic Regression (STARS1)

#Top 8 
model2A = LogisticRegression(solver='lbfgs',multi_class='ovr')
rfe = RFE(model2A, 8)
fit = rfe.fit(cleveland_f, cleveland_l)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

#Model 2B - Recursive Feature Elimination with Logistic Regression (STARS2)

#Top 8 
model2B = LogisticRegression(solver='lbfgs',multi_class='multinomial')
rfe = RFE(model2B, 8)
fit = rfe.fit(cleveland_f, cleveland_l)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

#Model 3 - Univariate Selection - Chi Squared

#Top 1-8
model3 = SelectKBest(score_func=chi2)
chi2fit = model3.fit(cleveland_f, cleveland_l)
print(chi2fit.scores_)

#Model 4 - Univariate Selection - F Classif

#Top 1-8
model4 = SelectKBest(score_func=f_classif)
ffit = model4.fit(cleveland_f, cleveland_l)
print(ffit.scores_)

#Model 5 - Bagged Decision Tree

#Top 1-8
model5 = ExtraTreesClassifier(n_estimators=100)
etcfit = model5.fit(cleveland_f, cleveland_l)
print(etcfit.feature_importances_)