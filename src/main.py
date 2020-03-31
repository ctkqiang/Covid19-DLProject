#!/usr/bin/env python
# John Melody Me
# Data Get from https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
import pandas
from pandas import read_csv
from datetime import datetime, date

currentDateTime = datetime.now()
statistic_data = "data\covid_19_data.csv"
names = ["No", "Date", "Province", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
dataset = read_csv(statistic_data, names=names)
# print(dataset.shape) #(10359, 8) (columns, row)
# print(dataset.head(50))
print(currentDateTime, "\n" ,"World Wide <data> \n\n ", dataset.describe)