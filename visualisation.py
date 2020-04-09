#!/usr/bin/env python
Copyright = """
                  Copyright 2020 © John Melody Me

      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at

                  http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      See the License for the specific language governing permissions and
      limitations under the License.
      @Author : John Melody Me
      @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
      @INPIREDBYGF: Cindy Tan Sin Dee <3
"""
import numpy as np
import pandas as pd
import os

print(Copyright, "\n\n")
for dirname, _, filenames in os.walk("data/Dataset"):
      for filename in filenames:
            print(os.path.join(dirname, filename))
print("\n")

import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import folium as fl
from datetime import datetime
from pathlib import Path
from sklearn.impute import SimpleImputer
sns.set()
#%matplotlib inline
pd.options.plotting.backend
pd.plotting.register_matplotlib_converters()

data = "data/Dataset/covid_19_data.csv"
covidData = pd.read_csv(data)
print("\n\n Covid_19_data HEAD: \n", covidData.head(), "\n\n Covid_19_data INFO: \n", covidData.info())

missing = covidData.isnull().sum()
missing[missing > 0]
print("\n\n INSPECTION: \n", missing)

imputer = SimpleImputer(strategy="constant")
impute_covid = pd.DataFrame(imputer.fit_transform(covidData), columns=covidData.columns)
print("\n\n IMPUTE_COVID_DATA HEAD: \n", impute_covid.head())
#CONVERSION :
impute_covid['ObservationDate'] = pd.to_datetime(impute_covid['ObservationDate'])
impute_covid['Last Update'] = pd.to_datetime(impute_covid['Last Update'])
impute_covid['Confirmed'] = pd.to_numeric(impute_covid['Confirmed'], errors='coerce')
impute_covid['Recovered'] = pd.to_numeric(impute_covid['Recovered'], errors='coerce')
impute_covid['Deaths'] = pd.to_numeric(impute_covid['Deaths'], errors='coerce')
# print("\n", impute_covid.info())

filename = "data/Dataset/COVID19_line_list_data.csv"
open_covid_data = pd.read_csv(filename)
print(open_covid_data.info())
mis_value = open_covid_data.isnull().sum()
mis_value[mis_value > 0 ]
# thresh_value = open_covid_data['date_confirmation'].isnull().sum()
# cols_interest_missing = [col for col in open_covid_data.columns if open_covid_data[col].isnull().sum()<=thresh_value]
# print(cols_interest_missing)
impute_covid['active_confirmed'] = impute_covid['Confirmed'].values - \
(impute_covid['Deaths'].values+impute_covid['Recovered'].values)
impute_covid.isnull().sum()[impute_covid.isnull().sum()>0]
print(impute_covid.info(), impute_covid.corr())

features = [['Confirmed', 'Deaths'], ['Confirmed', 'Recovered'], ['Recovered', 'Deaths'], \
            ['Confirmed', 'active_confirmed']]
values = [[impute_covid['Confirmed'], impute_covid['Deaths']],\
          [impute_covid['Confirmed'], impute_covid['Recovered']],\
          [impute_covid['Recovered'], impute_covid['Deaths']],\
          [impute_covid['Confirmed'], impute_covid['active_confirmed']]]

# fig = plt.figure(figsize=(20.5,10.5))
# fig.subplots_adjust(hspace=0.2, wspace=0.1)
# for i in range(1,5):
#     ax = fig.add_subplot(2, 2, i)
#     col = features[i-1]
#     val = values[i-1]
#     ax.scatter(val[0], val[1])
#     ax.set_xlabel(col[0])
#     ax.set_ylabel(col[1])
# #     ax.set_title('Feature curves')
# plt.show()

start_date = impute_covid.ObservationDate.min()
end_date = impute_covid.ObservationDate.max()
today = datetime.today()
print('Novel Covid-19 information:\n 1. Start date = {}\n 2. End date = {}'.format(start_date, end_date))
"""
[OUTPUT]
Novel Covid-19 information:
  1. Start date = 2020-01-22 00:00:00
  2. End date = 2020-03-30 00:00:00
"""
worldwide = impute_covid[impute_covid['ObservationDate'] == end_date]
nb_country = len(worldwide['Country/Region'].value_counts())
worldwide['Country/Region'].value_counts()
world = worldwide.groupby('Country/Region').sum()
world = world.sort_values(by=['Confirmed'], ascending=False)
# world.head()
print("\n\n")
print('================ Worldwide report ===============================')
print('== Information to {} on novel COVID-19 =========\n'.format(end_date))
print('Tota confirmed: {}\nTotal Deaths: {}\nTotal Recovered: {}\nTotal active confirmed: {}\n\
Total country Recorded: {} \n'.format(\
worldwide.Confirmed.sum(), worldwide.Deaths.sum(), worldwide.Recovered.sum(), worldwide.active_confirmed.sum(),\
                                     nb_country))
print('==================================================================')
print("\n\n")

TITLE = str("Covid-19 Visualisation 2020 From {} to {}".format(start_date, today))

# Confirmed Cases:
world.Confirmed.plot(kind='bar', title=TITLE, figsize=(20,8), logy=True, colormap='summer',legend=True)
plt.ylabel('Total Cases')
# plt.show()

# Recovered Cases:
world.Recovered.plot(kind='bar', title=TITLE, figsize=(20,8), logy=True, colormap='spring', legend=True)
plt.ylabel('Total Recovered')
# plt.show()

# Active Cases :
world.active_confirmed.plot(kind='bar', title=TITLE , figsize=(20,8), logy=True,\
                            colormap='winter', legend=True)
plt.ylabel('Total Active Cases')
# plt.show()

# Deaths Cases:
world.Deaths.plot(kind='bar', title=TITLE, figsize=(20,8), logy=True,\
                     colormap='autumn', legend=True)
plt.ylabel('Total Deaths')
# plt.show()

world_table = world.reset_index()
x = world_table[world_table['Country/Region'] == 'Malaysia']
big_7 = world_table[world_table['Confirmed'] >= x.iloc[0,1]]
big_7.style.background_gradient(cmap='viridis')
axs = big_7.plot('Country/Region', ['Confirmed', 'Deaths', 'Recovered', 'active_confirmed'], kind='barh',\
                 stacked=True, title='Country most affected by Covid-19',\
                 figsize=(20,10.5),colormap='rainbow_r', logx=True, legend=True)
pd.plotting.table(data=world_table, rowLabels=world.index, colLabels=world.columns, ax=axs)
plt.xlabel(' ')

time_obs = impute_covid.groupby('ObservationDate')['Confirmed'].aggregate([np.sum])
time_obs.columns = ['Confirmed']
time_obs.plot(figsize=(20,8), title='novel COVID-19 in the Worldwide', kind='bar')
plt.ylabel('Total Confirmed observation')

death_rate = impute_covid.groupby('ObservationDate')['Deaths'].aggregate([np.sum])
recovered_rate = impute_covid.groupby('ObservationDate')['Recovered'].aggregate([np.sum])
activecase_rate = impute_covid.groupby('ObservationDate')['active_confirmed'].aggregate([np.sum])
death_rate.columns = ['Death rate']
recovered_rate.columns = ['Recovered rate']
activecase_rate.columns = ['Active confirmed rate']
recovered_rate.plot(figsize=(15.5, 5), title='novel COVID-19 in the Worldwide', colormap='Greens_r', kind='bar')
plt.ylabel('Total patient')
plt.show()