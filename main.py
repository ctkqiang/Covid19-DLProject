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
import COVID19Py
from datetime import datetime
import random

covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()
location = str(covid19.getLocationByCountryCode("MY"))
data = covid19.getAll()
changes = covid19.getLatestChanges()
# print(data)
print(location)

file = "latestCovidForecast.json"
f = open(str(file), "a+")
for i in range(10):
      f.write(str(location))
      f.close()