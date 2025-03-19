# Ecom Data Analysis
# Data source:
# https://www.kaggle.com/datasets/cemeraan/fecom-inc-e-com-marketplace-orders-data-crm

# pip install pandas
import numpy as np
import pandas as pd

print("Hello world! I am Ecom Data Analysis by Sunseehray Tirazona")
print()

# format number to currency with $ and , up to 2 decimal places
def formatToCurrency(number):
    return '${:,.2f}'.format(number)

# Extract data from file
# https://pandas.pydata.org/docs/user_guide/10min.html#importing-and-exporting-data

# Customer List
path_customers = "ecomdataset/Fecom Inc Customer List.csv"
customers = pd.read_csv(path_customers, sep=";")

# Order List
# parsed order purchase timestamp to datetime for stretch / question 3
# How to turn string into datetime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html
path_orders = "ecomdataset/Fecom Inc Orders.csv"
orders = pd.read_csv(path_orders, sep=";", parse_dates=["Order_Purchase_Timestamp"])

# Order Payments
path_order_payments = "ecomdataset/Fecom Inc Order Payments.csv"
payments = pd.read_csv(path_order_payments, sep=";")

# QUESTION 1 - WHICH COUNTRY HAS THE BIGGEST SALES FOR THE PERIOD
# Group by country - how to group: https://pandas.pydata.org/docs/user_guide/10min.html#grouping
# Getting sum based on filters: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html

print("QUESTION 1: Which country had the biggest sales?")
print()
# merge orders and customer to see which country customer is from
orders_country = pd.merge(orders, customers, on="Customer_Trx_ID", how="inner")

# merge orders_country to see payment_value for each order
orders_country_payments = pd.merge(orders_country, payments, on="Order_ID", how="inner")

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
print(formatToCurrency(top_sales))
print()

# QUESTION 2 - Which gender has higher average spending in France?
print("QUESTION 2: Which gender has higher average spending in France?")
print()

# Aggregate by country 
# Filter France
print("France sales total:")
france_orders = orders_country[orders_country["Customer_Country"] == "France"]
france_sales = pd.merge(payments, france_orders, on="Order_ID", how="inner")
france_sales_total = france_sales["Payment_Value"].sum()
print(formatToCurrency(france_sales_total))
print()

orders_female = france_orders[france_orders["Gender"] == "Female"]
sales_female = pd.merge(orders_female, payments, on="Order_ID", how="inner")

print("FEMALES")
# female total sales
sales_female_total = sales_female["Payment_Value"].sum()
print("Total sales:")
print(formatToCurrency(sales_female_total))
# female average sales
sales_female_average = sales_female["Payment_Value"].mean()
print("Average sales:")
print(formatToCurrency(sales_female_average))

print() 

orders_male = france_orders[france_orders["Gender"] == "Male"]
sales_male = pd.merge(orders_male, payments, on="Order_ID", how="inner")

print("MALES")
# male total sales
sales_male_total = sales_male["Payment_Value"].sum()
print("Total sales:")
print(formatToCurrency(sales_male_total))
# male average sales
sales_male_average = sales_male["Payment_Value"].mean()
print("Average sales:")
print(formatToCurrency(sales_male_average))

print()

# Result
print("RESULT:")
if (sales_female_average > sales_male_average):
    print("Females in France have a higher average spending compared to males.")
else:
    print("Males in France have a higher average spending compared to females.")

# STRETCH QUESTION 3 - Which MONTH generated lowest sales in 2024?
# Stretch challenge
# Aggregate information by month, sum sales, then get the one with the lowest value.
# Filter sales by year
print()
print("QUESTION 3 - Which month generated the lowest sales in 2024?")

# Merge orders with payments to see date and payment value together
paid_orders = pd.merge(orders, payments, on="Order_ID", how="inner")

# Get orders for 2024 only
paid_orders2024 = paid_orders[paid_orders["Order_Purchase_Timestamp"].dt.year == 2024]
paid_orders2024 = paid_orders2024.sort_values("Order_Purchase_Timestamp")

# Verifying sum for month 10
print(paid_orders2024[["Order_ID", "Order_Purchase_Timestamp", "Payment_Value"]].tail(5))

# Aggregate by month
month_sales_2024 = paid_orders2024.groupby(paid_orders2024["Order_Purchase_Timestamp"].dt.month)[["Payment_Value"]].sum().rename(columns={ "Payment_Value": "Month_Total" })
print("Sales by month:")
print(month_sales_2024)
print()

# Find MIN value
# return month with lowest sales
top_month = month_sales_2024["Month_Total"].idxmin()
print("Which month has the lowest sales?")
print(top_month)
print()

# return value of lowest sales
top_month_sales = month_sales_2024["Month_Total"].min()
print("How much was that month's sales?")
print(formatToCurrency(top_month_sales))
print()

print("END OF DATA ANALYSIS. THANK YOU!")

