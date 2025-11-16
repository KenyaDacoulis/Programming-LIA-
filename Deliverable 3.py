# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 17:28:21 2025

@author: Kenya Dacoulis, Lindsay Joseph, Ava Binetti 
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('product_sales_dataset_final.csv')

#----PART 2: PRELIMINARY STEPS----

# a)

# number of rows and columns
shape = data.shape
print(shape)
# descriptive stats
stats = data.describe()
print(stats)
# summary of dataset
info = data.info()
print(info)


# b) duplicates

duplicates = data.duplicated().value_counts()
print(duplicates)
# There are no duplicates in this dataset

# c) empty values

empty_values = data.isnull().sum()
print(empty_values)
# There are no empty values in the dataset

# d)  

data['Date'] = pd.to_datetime(data['Order_Date'])

# Addition of columns representing time periods

# seasons
data['Order_Date'] = pd.to_datetime(data['Order_Date'])

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

    
data['Season'] = data['Order_Date'].dt.month.apply(get_season)
#the def function was used to categorize the dates into blocks of seasons. The link that shows where the function was found and understood is seen in the lab report.  

# Month

data['Month'] = data['Date'].dt.month

# Quarter

data['Quarter'] = data['Date'].dt.quarter

# Year

data['Year'] = data['Date'].dt.year


#----PART 3: Univariate non-graphical EDA----

#--NUMERICAL DATA--

# 1: Quantity

info_quantity = data['Quantity'].describe()
print(info_quantity)
median_quantity = data['Quantity'].median()
print('median quantity: ', median_quantity)
mode_quantity = data['Quantity'].mode()
print('mode quantity: ', mode_quantity)
varience_quantity = data['Quantity'].var()
print('varience quantity:', varience_quantity)
skewness_quantity = data['Quantity'].skew()
print('skewness quantity:', skewness_quantity)
kurtosis_quantity = data['Quantity'].kurtosis()
print('kurtosis quantity:', kurtosis_quantity)


# 2: Unit Price
info_unit_price = data[" Unit_Price "].describe()
print(info_unit_price)
median_unit_price = data[' Unit_Price '].median()
print('median unit price: ',median_unit_price)
mode_unit_price = data[' Unit_Price '].mode()
print('mode unit price: ', mode_unit_price)
varience_unit_price = data[' Unit_Price '].var()
print('varience unit price:', varience_quantity)
skewness_unit_price = data[' Unit_Price '].skew()
print('skewness unit price:', skewness_quantity)
kurtosis_unit_price = data[' Unit_Price '].kurtosis()
print('kurtosis unit price:', kurtosis_unit_price)

# 3: Revenue

info_revenue = data[' Revenue '].describe()
print(info_revenue)
median_revenue = data[' Revenue '].median()
print('median revenue: ', median_revenue)
mode_revenue = data[' Revenue '].mode()
print('mode revenue: ', mode_revenue)
varience_revenue = data[' Revenue '].var()
print('varience revenue:', varience_revenue)
skewness_revenue = data[' Revenue '].skew()
print('skewness revenue:', skewness_revenue)
kurtosis_revenue = data[' Revenue '].kurtosis()
print('kurtosis revenue:', kurtosis_revenue)

# 4: Profit

info_profit = data[' Profit '].describe()
print(info_profit)
median_profit = data[' Profit '].median()
print('median profit: ', median_profit)
mode_profit = data[' Profit '].mode()
print('mode profiy: ', mode_profit)
varience_profit = data[' Profit '].var()
print('varience profit:', varience_profit)
skewness_profit = data[' Profit '].skew()
print('skewness profit:', skewness_profit)
kurtosis_profit = data[' Profit '].kurtosis()
print('kurtosis profit:', kurtosis_profit)


# 5: Date**

#--CATEGORICAL DATA--

# 1: Customer_Name

frequency_counts_customer_name = data['Customer_Name'].value_counts()
print('frequency customer name:', frequency_counts_customer_name)
proportion_customer_name = (frequency_counts_customer_name/(data['Customer_Name'].count()))
print('proportion customer name:', proportion_customer_name)
mode_customer_name = data['Customer_Name'].mode()
print('mode customer name:',mode_customer_name)
unique_customer_name = data['Customer_Name'].nunique()
print('number unique customer names:', unique_customer_name)

# 2: City

frequency_counts_city = data['City'].value_counts()
print('frequency city:', frequency_counts_city)
proportion_city = (frequency_counts_city/(data['City'].count()))
print('proportion city:', proportion_city)
mode_city = data['City'].mode()
print('mode city:', mode_city)
unique_city = data['City'].nunique()
print('number unique cities:', unique_city)

# 3: State        

frequency_counts_state = data['State'].value_counts()
print('frequency state:', frequency_counts_state)
proportion_state = (frequency_counts_state/(data['State'].count()))
print('proportion state:', proportion_state)
mode_state = data['State'].mode()
print('mode state:', mode_state)
unique_state = data['State'].nunique()
print('number unique states:', unique_state)

# 4: Region      

frequency_counts_region = data['Region'].value_counts()
print('frequency region:', frequency_counts_region)
proportion_region = (frequency_counts_region/(data['Region'].count()))
print('proportion region:', proportion_region)
mode_region = data['Region'].mode()
print('mode region:', mode_region)
unique_region = data['Region'].nunique()
print('number unique regions:', unique_region)

# 5: Country        

frequency_counts_country = data['Country'].value_counts()
print('frequency country:', frequency_counts_country)
proportion_country = (frequency_counts_country/(data['Country'].count()))
print('proportion country:', proportion_country)
mode_country = data['Country'].mode()
print('mode country:', mode_country)
unique_country = data['Country'].nunique()
print('number unique countries:', unique_country)

# 6: Category      

frequency_counts_category = data['Category'].value_counts()
print('frequency category:', frequency_counts_category)
proportion_category = (frequency_counts_category/(data['Category'].count()))
print('proportion category:', proportion_category)
mode_category = data['Category'].mode()
print('mode category:', mode_category)
unique_category = data['Category'].nunique()
print('number unique categories:' , unique_category)

# 7: Sub_Category   

frequency_counts_sub_category = data['Sub_Category'].value_counts()
print('frequency sub category:', frequency_counts_sub_category)
proportion_sub_category = (frequency_counts_sub_category/(data['Sub_Category'].count()))
print('proportion sub category:', proportion_sub_category)
mode_sub_category = data['Sub_Category'].mode()
print('mode sub category:', mode_sub_category)
unique_sub_category = data['Sub_Category'].nunique()
print('number unique sub categories:' , unique_sub_category)

# 8: Product_Name

frequency_counts_product_name = data['Product_Name'].value_counts()
print('frequency product name:', frequency_counts_product_name)
proportion_product_name = (frequency_counts_product_name/(data['Product_Name'].count()))
print('proportion product name:', proportion_product_name)
mode_product_name = data['Product_Name'].mode()
print('mode product name:', mode_product_name)
unique_product_name = data['Product_Name'].nunique()
print('number unique product names:' , unique_product_name)


#----PART 4: Univariate graphical EDA----

numerical_data = data[['Quantity', ' Unit_Price ', ' Revenue ', ' Profit ']]
for i in numerical_data:
# a) Custom and appropriate number of bins
    if i != 'Quantity':
        sns.displot(data, x = i, bins = 10)
# b) Conditioning on other variables
        sns.displot(data, x = i, hue = 'Region',  palette= 'bright') 
# c) Stacked histogram        
        sns.displot(data, x = i, hue = 'Quarter', multiple = 'stack', palette = 'bright')     
# d) Dodge bars
        sns.displot(data, x = i, hue = 'Year', multiple = 'dodge', bins = 50, palette= 'bright') 
# e) Normalized histogram statistics
        sns.displot(data, x = i, stat = 'density', common_norm = False) 
# f) KDE
        sns.displot(data, x = i, kind = 'kde', bw_adjust = 1.5) 
# g) Empirical cumulative distributions
        sns.displot(data, x = i, hue = 'Category', kind = 'ecdf', palette= 'bright')
    else:
        sns.displot(data, x = i, discrete = True) # a)
        sns.displot(data, x = i, hue = 'Region', discrete = True, palette= 'bright') # b) 
        sns.displot(data, x = i, hue = 'Quarter', multiple = 'stack', discrete = True, palette= 'bright') # c) 
        sns.displot(data, x = i, hue = 'Year', multiple = 'dodge',discrete = True, palette= 'bright') # d)
        sns.displot(data, x = i, stat = 'density', common_norm = False, discrete = True) # e)
        sns.displot(data, x = i, kind = 'kde', bw_adjust = 1.5) # f)
        sns.displot(data, x = i, hue = 'Category', kind = 'ecdf', palette= 'bright') # g)


#-----Part 5:  Multivariate non-graphical EDA----------

Cat_state_table= pd.crosstab(data['State'], data['Category'], normalize='index') * 100
print(Cat_state_table)

Sub_Cat_Year_table= pd.crosstab(data['Sub_Category'], data['Year'], normalize='index') * 100
print(Sub_Cat_Year_table)

Reg_season_table= pd.crosstab(data['Region'], data['Season'], normalize='index') * 100 
print(Reg_season_table)

multvariable_table= pd.crosstab([data['Category'], data['Region']], data['Sub_Category'], normalize='index') * 100
print(multvariable_table)


#----PART 6: Multivariate graphical EDA----

    
# 6.1.Visualizing statistical relationships (5 plots): 

# a) Which category makes the most profit?
sns.displot(data = data, x = ' Profit ', col = 'Category' )

# b) 

sns.relplot(data=data.sample(1000), x=' Revenue ', y=' Profit ', hue='Season', size='Quantity', col= 'Category', kind='scatter')
plt.show()


# c)  What is the profit distribution per month for 2023 and 2024?

sns.relplot(data = data, x = 'Month', y = ' Profit ', kind = 'line', hue = 'Year', palette = 'bright')
plt.show()


# d) Which category has the most profit variation?

sns.barplot(data=data, x='Category', y=' Profit ', errorbar='sd')
plt.show()

# e) Is there a linear relationship between unit price and profit?

sns.lmplot(data=data.sample(800), x= ' Unit_Price ', y=' Profit ', hue='Season')
g=sns.FacetGrid(data=data.sample(800), col='Season', hue= 'Season') # whats going on here
plt.show()


# 6.2.Visualizing categorical data (10 plots):
    
#a) Quantity per category
sns.stripplot(data=data.sample(800), x='Category', y=' Unit_Price ', jitter=True,)
plt.show()

#b)  Quantity per region
sns.stripplot(data=data.sample(800), x='Region', y='Quantity', jitter=False,)
plt.show()

# c) Does the revenue vary by region and does it vary by quarter of the year?

sns.catplot(data = data.sample(1000), x = 'Region', y = ' Revenue ', col = 'Quarter', kind = 'swarm')
plt.show()
# sample of 1000 orders because too much data to make plot thats legible

#d ) Does profit vary by category across quarters of the year?

sns.catplot(data = data.sample(800), x = ' Profit ', y = 'Category', hue = 'Quarter', kind = 'box')
plt.show()

#e) Revenue per category

sns.boxenplot(data=data, x='Season', y=' Revenue ', palette='pastel') 
plt.show()

# f) what is the profit distribution across categories for 2023 and 2024

sns.catplot(data = data.sample(800), x = ' Profit ', y = 'Category', hue = 'Year', kind = 'violin', split = True, inner = 'stick', bw_adjust = 5, palette = 'pastel')
plt.show()

# g) Do prices rise drastically during different times of the year?

sns.violinplot(data=data.sample(1000), x='Season', y=' Unit_Price ', inner= None)
sns.stripplot(data=data.sample(500), x ='Season', y =' Unit_Price ', color= 'pink')
plt.show()

# h) Revenue Category 

sns.barplot(data=data, x='Category', y=' Revenue ', hue='Region', ci=97,)
plt.show()

# i) 

sns.pointplot(data=data, x='Quantity', y=' Unit_Price ', hue='Year', ci=90, linestyles='--', palette= 'bright')
plt.show()

# j) Is there a season where people tend to consume more?

sns.countplot(data=data, x='Season', hue= "Season", palette= 'pastel')
plt.show()


# 6.3. Visualizing bivariate distributions (3 plots): 

#a)What can the relationship between revenue and profit tell us about sales dynamics?
sns.histplot(data=data.sample(1000), x=' Unit_Price ', y=' Profit ', bins=25, cmap='coolwarm')
plt.show()

#b) Does higher revenue lead to higher profit?
sns.displot(data = data.sample(1000), x = ' Revenue ', y = ' Profit ', kind = 'kde', thresh = 0.05, levels = 7) 
plt.show()

#c) Do people tend to by more of products that cost less and is it consistant throughout both years?

sns.displot(data = data.sample(1000), x = ' Unit_Price ', y = 'Quantity', col = 'Year', kind = 'kde') 
plt.show()




