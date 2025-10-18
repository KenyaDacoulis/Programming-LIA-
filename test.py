# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#----BAR GRAPH-----

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


#----PIE CHART----
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


#----SUBPLOTS----

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("animal-data-1.csv", nrows= 100)

# subplot 1 is a bar graph showing amount per species type, subplot 2 is a bar graph showing the reason they were taken in. this will show  which species are more commonly left for specific reasons.
plt.subplots
     
fig, axs = plt.subplots(1, 2,)
x = data['speciesname'].value_counts().index
y = data['speciesname'].value_counts().values

axs[0].bar(x,y, color = "yellow")
axs[0].set_xlabel("Species")
axs[0].set_ylabel("Count")
axs[0].set_title("Number of Animals by Species")

# Subplot 2: Intake Reason
x = data['intakereason'].value_counts().index  
y = data['intakereason'].value_counts().values 

axs[1].bar(x,y, color = "purple")
axs[1].set_title('Count by Intake Reason')
axs[1].set_xlabel("Reason")
axs[1].set_ylabel("Count")

