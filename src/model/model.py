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
# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
sns.countplot('Deaths',data=sales_data,hue = 'Index')
sns.despine(offset=10, trim=True)