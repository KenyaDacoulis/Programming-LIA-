# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("animal-data-1.csv", nrows= 100)


# bar graph showing number of animals per species for first 100 rows of data               
x = data['speciesname'].value_counts().index
y = data['speciesname'].value_counts().values

plt.bar(x,y, color = "cornflowerblue")
plt.xlabel("Species")
plt.ylabel("Count")
plt.title("Number of Animals by Species")
plt.show()



