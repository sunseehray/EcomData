# Ecom Data Analysis

import numbers as np
import pandas as pd

# Questions to answer:
# Which country has the biggest sales for the period?
# Which gender has higher average spending in France?

# Aggregate information by country as sum of sales, then get the country with the highest sum
# Aggregate information by gender and filter by country, France then sum sales by gender, compare

# Stretch challenge
# try graphing if time permits, if not, answer third question:
# Which MONTH generated lowest sales?
# Aggregate information by month, sum sales, then get the one with the lowest value.

print("Hello world!")


# GET DATA
# Data source:
# https://www.kaggle.com/datasets/cemeraan/fecom-inc-e-com-marketplace-orders-data-crm

# Extract data from file
# https://pandas.pydata.org/docs/user_guide/10min.html#importing-and-exporting-data

path_customers = "ecomdataset/Fecom Inc Customer List.csv"
customers = pd.read_csv("ecomdataset/Fecom Inc Customer List.csv", sep=";")

# QUESTION 1
# Group by country - how to group: https://pandas.pydata.org/docs/user_guide/10min.html#grouping
# Getting sum based on filters: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html

# To get orders by country, I need customer information
# From the customer information, I can get the Customer_Country

countries = customers["Customer_Country"].dropna().unique()
print(len(countries))

# 27 countries
# ['France' 'Poland' 'Netherlands' 'Italy' 'Sweden' 'Spain' 'Germany'
#  'Czechia' 'Belgium' 'Greece' 'Switzerland' 'United Kingdom' 'Austria'
#  'Norway' 'Portugal' 'Turkey' 'Luxembourg' 'Slovakia' 'Serbia' 'Slovenia'
#  'Latvia' 'Lithuania' 'Denmark' 'Croatia' 'Estonia' 'Andorra' 'Finland']

# QUESTION 2
# Aggregate by country 
# Filter France
# Aggregate by gender
# Sum? or does aggregate get the sum automatically?

# STRETCH QUESTION 3
# Filter sales by year
# Aggregate by month
# Find MAX value

# Try graphing
