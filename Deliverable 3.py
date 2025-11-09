# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 17:28:21 2025

@author: Kenya Dacoulis
"""

import pandas as pd
import seaborn as sns

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


#----PART 3: Univariate non-graphical EDA----

#--NUMERICAL DATA--

# 1: Quantity

info_quantity = data['Quantity'].describe()
print(info_quantity)
varience_quantity = data['Quantity'].var()
print('varience quantity:', varience_quantity)
skewness_quantity = data['Quantity'].skew()
print('skewness quantity:', skewness_quantity)
kurtosis_quantity = data['Quantity'].kurtosis()
print('kurtosis quantity:', kurtosis_quantity)


# 2: Unit Price
info_unit_price = data[" Unit_Price "].describe()
print(info_unit_price)
varience_unit_price = data[' Unit_Price '].var()
print('varience unit price:', varience_quantity)
skewness_unit_price = data[' Unit_Price '].skew()
print('skewness unit price:', skewness_quantity)
kurtosis_unit_price = data[' Unit_Price '].kurtosis()
print('kurtosis unit price:', kurtosis_unit_price)

# 3: Revenue

info_revenue = data[' Revenue '].describe()
print(info_revenue)
varience_revenue = data[' Revenue '].var()
print('varience revenue:', varience_revenue)
skewness_revenue = data[' Revenue '].skew()
print('skewness revenue:', skewness_revenue)
kurtosis_revenue = data[' Revenue '].kurtosis()
print('kurtosis revenue:', kurtosis_revenue)

# 4: Profit

info_profit = data[' Profit '].describe()
print(info_profit)
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

# 1: Quantity

sns.displot(data = data, x = 'Quantity', discrete = True)

# 2: Unit Price

sns.displot(data = data, x = ' Unit_Price ', hue = 'Category', element = 'step')

# 3: Revenue

sns.displot(data = data, x = ' Revenue ', kind = 'kde',  bw_adjust = .5)

# 4: Profit

sns.displot(data = data, x = ' Profit ', hue = 'Region')




#-----Part 5:  Multivariate non-graphical EDA----------

pd.crosstab(data['State'], data['Category'], normalize='index') * 100


pd.crosstab(data['Sub_Category'], data['Product_Name'], normalize='index') * 100


pd.crosstab(data['Region'], data['Quantity'], normalize='index') * 100


pd.crosstab([data['Category'], data['Region']], data['Sub_Category'], normalize='index') * 100







