# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("animal-data-1.csv", nrows= 100)

#PART 3
# This code eliminated the information of animals that have no microchip. It works by going over each value in the column and if it is empty (has no value) it removes it 

for i in data.index:
    value = data["identichipnumber"][i]
    if value != value:
        data = data.drop(i)
        clean_data = data

print(clean_data)

#PART 4




#----BAR GRAPH-----



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


#----SCATTER PLOT #2-----

#Scatterplot graph showing the intake and movement date of animals. It shows hol long they were at the shelter.
#The dots closset to the diagonal are those who spent the least amount of time at the shelter.

# Converting dates to datetime format
data["intakedate"] = pd.to_datetime(data["intakedate"])
data["movementdate"] = pd.to_datetime(data["movementdate"])

# Droping rows missing either date
data = data.dropna(subset=["intakedate", "movementdate"])

# Scatter plot
x = data["intakedate"]
y=  data["movementdate"]
plt.scatter(x,y, color = 'blue')
plt.title("Intake Date vs. Movement Date")
plt.xlabel("Intake Date")
plt.ylabel("Movement Date")
plt.grid(axis = 'y')


# Diagonal reference line
a = [x.min(), x.max()]
b = [y.min(), y.max()]
plt.plot(a,b, color = 'red', linestyle = '--')
plt.show()


#----HISTOGRAM #2-----

#Histogram showing the amount of animals taken in throughout the years

#converting dates to proper format
data['intakedate'] = pd.to_datetime(data["intakedate"])
data['intake_year'] = data['intakedate'].dt.year

#Histogram 
x = data['intake_year']
plt.hist(x, color = 'purple')
plt.xlabel("Year")
plt.ylabel("Number of Animals")
plt.title("Number of Animals Taken In per year")
plt.show()
