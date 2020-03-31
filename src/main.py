#!/usr/bin/env python
# John Melody Me
import pandas
from pandas import read_csv
from datetime import datetime, date
import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []

currentDateTime = datetime.now()
statistic_data = "data/covid_19_data.csv"
names = ["No", "Date", "Province", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
dataset = read_csv(statistic_data, names=names)
with open("data/deaths.csv", "r") as COVIDDATA:
      display = csv.reader(COVIDDATA, delimiter=",")
      for row in display:
            x.append(int(row[0]))
            y.append(int(row[1]))

# print(dataset.shape) #(10359, 8) (columns, row)
# print(dataset.head(50))
print(currentDateTime, "\n" ,"World Wide <data> \n\n ", dataset.describe)
# Class Distribution:
print(currentDateTime, "\n", dataset.groupby(names).size())
# Graph:
plt.title("COVID 19 DEATHS <22 JAN 2020 TO 31 MAC 2020> STATISTICS")
plt.xlabel("Index")
plt.ylabel("Deaths")
# plt.zlabel("Recovered")
plt.plot(x,y)
plt.legend(x, y)
plt.Line2D(x,y)
plt.show()