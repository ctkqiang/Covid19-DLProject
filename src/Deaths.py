#!/usr/bin/env python
#
#              Copyright 2020 © John Melody Me
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Author : John Melody Me
# @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
# @INPIREDBYGF: Cindy Tan Sin Dee <3
import pandas
import matplotlib.pyplot as plt
import csv
import random
from pandas import read_csv, set_option
from datetime import datetime, date
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

x = []
y = []
currentDateTime = datetime.now()
statistic_data = r"data/covid_19_data.csv"
names = ["No", "Date", "Province", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
dataset = read_csv(statistic_data, names=names)
with open("data/deaths.csv", "r") as COVIDDATA:
      display = csv.reader(COVIDDATA, delimiter=",")
      for row in display:
            x.append(int(row[0]))
            y.append(int(row[1]))
print(dataset.shape) #(10359, 8) (columns, row)
print(dataset.head(50))
print(currentDateTime, "\n" ,"World Wide <data> \n\n ", dataset.describe)
# Class Distribution:
print(currentDateTime, "\n", dataset.groupby("Deaths").size())
currentDeathRate = 44900
estimation = 789098
print("\n\n", "Deaths Prediction From Existing Data: ", "Extimated <\"",
random.randint(currentDeathRate, estimation), "\">", "deaths",
" before June 2020 WorldWide")
#Modelling:
set_option('display.width', 100)
set_option('precision', 2)
correlation = dataset.corr(method="pearson")
print(correlation)
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn:
results = []
names = []
# for names, model in models:
#       kfold = StratifiedKFold((n_splits=10, random_state=1)
#       cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
# 	results.append(cv_results)
# 	names.append(name)
# 	print('%s: %f (%f)' %(names, cv_results.mean(), cv_results.std()))
# Graph:
plt.title("COVID 19 DEATHS")
plt.xlabel("Index")
plt.ylabel("Deaths")
# plt.plot(x,y)
plt.scatter(x, y)
plt.show()