# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("animal-data-1.csv", nrows= 100)


#pie chart showing the most common intake reasons for the first 100 rows of data
#x: reasons( abandoned ,moving etc.) y: count(as a %)

labels = data['intakereason'].value_counts().index   
size = data['intakereason'].value_counts().values  

plt.pie (size,autopct='%1.1f%%')
plt.title("Animals Intake Reason")
plt.legend(labels=labels) #legend so that the sections are clearly defined 
plt.show()

