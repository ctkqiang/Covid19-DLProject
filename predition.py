#!/usr/bin/env python
import numpy as np
import pandas as pd
import os

for dirname, _, filenames in os.walk("/data/covid19"):
      for filename in filenames:
            print(os.path.join(dirname, filename))