# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("animal-data-1.csv", nrows= 100)



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

# bar graph showing number of animals per species for first 100 rows of data               
x = data['speciesname'].value_counts().index
y = data['speciesname'].value_counts().values

plt.bar(x,y, color = "cornflowerblue")
plt.xlabel("Species")
plt.ylabel("Count")
plt.title("Number of Animals by Species")
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


#----SCATTER PLOT-----

data['is_adopted'] = (data['movementtype'] == 'Adoption').astype(int)
x1 = range(len(data))

plt.scatter(x1, data['is_adopted'])
plt.xlabel('Animal Number')
plt.ylabel('Adoption Status (1 = Adopted, 0 = Not Adopted)')
plt.title('Scatter Plot: Adoption Status of Animals')

plt.show()



