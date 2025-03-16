# Ecom Data Analysis
# Data source:
# https://www.kaggle.com/datasets/cemeraan/fecom-inc-e-com-marketplace-orders-data-crm

# pip install pandas
import pandas as pd

print("Hello world! I am Ecom Data Analysis by Sunseehray Tirazona")
print()

# Extract data from file
# https://pandas.pydata.org/docs/user_guide/10min.html#importing-and-exporting-data

# Customer List
path_customers = "ecomdataset/Fecom Inc Customer List.csv"
customers = pd.read_csv(path_customers, sep=";")

# Order List
path_orders = "ecomdataset/Fecom Inc Orders.csv"
orders = pd.read_csv(path_orders, sep=";")

# Order Payments
path_order_payments = "ecomdataset/Fecom Inc Order Payments.csv"
payments = pd.read_csv(path_order_payments, sep=";")

# QUESTION 1 - WHICH COUNTRY HAS THE BIGGEST SALES FOR THE PERIOD
# Group by country - how to group: https://pandas.pydata.org/docs/user_guide/10min.html#grouping
# Getting sum based on filters: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html

# Get country from the Customer List.csv
# Look for Customer_Country

# countries = customers["Customer_Country"].dropna().unique()
# print("Countries:")
# print(countries)
# print()

# 27 countries
# ['France' 'Poland' 'Netherlands' 'Italy' 'Sweden' 'Spain' 'Germany'
#  'Czechia' 'Belgium' 'Greece' 'Switzerland' 'United Kingdom' 'Austria'
#  'Norway' 'Portugal' 'Turkey' 'Luxembourg' 'Slovakia' 'Serbia' 'Slovenia'
#  'Latvia' 'Lithuania' 'Denmark' 'Croatia' 'Estonia' 'Andorra' 'Finland']

# merge orders and customer to see which country customer is from
orders_country = pd.merge(orders, customers, on="Customer_Trx_ID", how="inner")

# merge orders_country to see payment_value for each order
orders_country_payments = pd.merge(orders_country, payments, on="Order_ID", how="inner")

print("QUESTION 1: Which country had the biggest sales?")
print()
# group by country and get total sales for each using sum()
country_sales = orders_country_payments.groupby("Customer_Country")[["Payment_Value"]].sum().rename(columns={"Payment_Value": "Total_Sales"})
country_sales = country_sales.sort_values(by="Total_Sales", ascending=False)
print("Sales by Country:")
print(country_sales)
print()

# return country with biggest sales
top_country = country_sales["Total_Sales"].idxmax()
print("Which country has the biggest sales?")
print(top_country)
print()

# return value of biggest sales
top_sales = country_sales["Total_Sales"].max()
print("How much was that country's sales?")
print(top_sales)
print()

print("QUESTION 2: Which gender has higher average spending in France?")

# QUESTION 2 - Which gender has higher average spending in France?
# Aggregate by country 
# Filter France

print("France sales total:")
france_orders = orders_country[orders_country["Customer_Country"] == "France"]
france_sales = pd.merge(payments, france_orders, on="Order_ID", how="inner")
france_sales_total = france_sales["Payment_Value"].sum()
print(france_sales_total)
print()

orders_female = france_orders[france_orders["Gender"] == "Female"]
sales_female = pd.merge(orders_female, payments, on="Order_ID", how="inner")

# female total sales
sales_female_total = sales_female["Payment_Value"].sum()
print("Total sales from females in France:")
print(sales_female_total)
# female average sales
sales_female_average = sales_female["Payment_Value"].mean()
print("Average sales from females in France:")
print(sales_female_average)

orders_male = france_orders[france_orders["Gender"] == "Male"]
sales_male = pd.merge(orders_male, payments, on="Order_ID", how="inner")

# male total sales
sales_male_total = sales_male["Payment_Value"].sum()
print("Total sales from males in France:")
print(sales_male_total)
# male average sales
sales_male_average = sales_male["Payment_Value"].mean()
print("Average sales from males in France")
print(sales_male_average)

# Aggregate by gender
# Sum? or does aggregate get the sum automatically?

# STRETCH QUESTION 3
# Filter sales by year
# Aggregate by month
# Find MAX value

# Stretch challenge
# Question 3 - Which MONTH generated lowest sales in 2024?
# Aggregate information by month, sum sales, then get the one with the lowest value.

# Try graphing if time permits

print("---------Just backend stuff--------------")
# get from Orders list of orders where year is 2023
orders_2023 = orders[orders["Order_Approved_At"].astype(str).str[:4] == "2023"].shape[0]

print("2023 orders: ")
# 44973
print(orders_2023)

print("All orders:")
# 99441
print(len(orders))