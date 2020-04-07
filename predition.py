#!/usr/bin/env python
import numpy as np
import pandas as pd
from pandas import read_csv, set_option
import matplotlib.pyplot as plt
import os
import csv


stateData = r"data/Data.csv"
data = read_csv(stateData)
x = ["Date"]
y = data
print(data)
print("data.describe() : \n\n ", data.describe())
# print(data.groupby("States").size())
