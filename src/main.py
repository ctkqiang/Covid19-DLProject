#!/usr/bin/env python
import pandas
from pandas import read_csv

statistic_data = "data\covid_19_data.csv"
header = ["No", "Date", "Province", "Country", "Update", "Confirmed", "Deaths", "Recovered"]
dataset = read_csv(statistic_data, names=header)