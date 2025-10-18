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


# 1 plot of any type containing data from more than 1 array using different colors and line styles.

data['is_adopted'] = data['movementtype'] == 'Adoption'
top5_species = data['speciesname'].value_counts().head(5).index
data_top5 = data[data['speciesname'].isin(top5_species)]

adoption_rate = data_top5.groupby('speciesname')['is_adopted'].mean() * 100
colors = ['red', 'blue', 'green', 'orange', 'purple']
adoption_rate.plot(kind='bar', color=colors)

plt.title('Adoption Rate by Species (Top 5)')
plt.ylabel('Adoption Rate')
plt.show()


#pie chart showing the most common intake reasons for the first 100 rows of data
#x: reasons( abandoned ,moving etc.) y: count(as a %)

labels = data['intakereason'].value_counts().index   
size = data['intakereason'].value_counts().values  

plt.pie (size,autopct='%1.1f%%')
plt.title("Animals Intake Reason")
plt.legend(labels=labels) #legend so that the sections are clearly defined 
plt.show()