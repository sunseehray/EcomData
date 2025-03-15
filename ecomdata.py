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
customers = pd.read_csv(path_customers, sep=";")

path_orders = "ecomdataset/Fecom Inc Orders.csv"
orders = pd.read_csv(path_orders, sep=";")

path_order_payments = "ecomdataset/Fecom Inc Order Payments.csv"
payments = pd.read_csv(path_order_payments, sep=";")

# QUESTION 1 - WHICH COUNTRY HAS THE BIGGEST SALES FOR THE PERIOD
# Group by country - how to group: https://pandas.pydata.org/docs/user_guide/10min.html#grouping
# Getting sum based on filters: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html

# To get orders by country, I need customer information
# From the customer information, I can get the Customer_Country

# Figure out how to merge there three data frames so I can get a list of orders by country and payment value !!!!!!

# merge orders and customer to see which country customer is from
orders_country = pd.merge(orders, customers, on="Customer_Trx_ID", how="inner")

# merge orders_country to see payment_value for each order
orders_country_payments = pd.merge(orders_country, payments, on="Order_ID", how="inner")

# sales by country -- I DID IT!!!!
country_sales = orders_country_payments.groupby("Customer_Country")[["Payment_Value"]].sum()
print(country_sales)

# this shows the maximum payment_value, but how do I return the name of the country that has that maximum value?
top_country = country_sales.max()
print(top_country)

countries = customers["Customer_Country"].dropna().unique()
print("Num of countries:")
print(len(countries))

# 27 countries
# ['France' 'Poland' 'Netherlands' 'Italy' 'Sweden' 'Spain' 'Germany'
#  'Czechia' 'Belgium' 'Greece' 'Switzerland' 'United Kingdom' 'Austria'
#  'Norway' 'Portugal' 'Turkey' 'Luxembourg' 'Slovakia' 'Serbia' 'Slovenia'
#  'Latvia' 'Lithuania' 'Denmark' 'Croatia' 'Estonia' 'Andorra' 'Finland']

# get from Orders list of orders where year is 2023
orders_2023 = orders[orders["Order_Approved_At"].astype(str).str[:4] == "2023"].shape[0]

print("2023 orders: ")
# 44973
print(orders_2023)

print("All orders:")
# 99441
print(len(orders))

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
