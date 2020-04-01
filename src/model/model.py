import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, date

title = "Deaths Rate Covid-19 <22 JAN 2020 to 31 MAC 2020> Statistics"
currentDateTime = datetime.now()
datasets = "data/covid_19_data.csv"
CovidData = pd.read_csv(datasets)
CovidData.head() # show the first few records of the data set
print(title, "\t", currentDateTime, "\n\n", CovidData)
print(CovidData.head(n=10), CovidData.tail()) # show the first (n) records of the data set
print(CovidData.dtypes) # datatypes
