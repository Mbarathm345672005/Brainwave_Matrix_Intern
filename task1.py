import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv', encoding='ISO-8859-1')

print("Dataset Head:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

top_products = df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products.head(10))

plt.figure(figsize=(10, 6))
df.groupby('ORDERDATE')['SALES'].sum().plot(kind='line', title='Sales Trend Over Time')
plt.ylabel('Total Sales')
plt.xlabel('Order Date')
plt.show()

sales_by_category = df.groupby('PRODUCTLINE')['SALES'].sum()

print("\nSales by Category:")
print(sales_by_category)

plt.figure(figsize=(8, 6))
sales_by_category.plot(kind='bar', title='Total Sales by Category')
plt.ylabel('Total Sales')
plt.show()

top_5_products = top_products.head(5)

plt.figure(figsize=(8, 6))
top_5_products.plot(kind='bar', title='Top 5 Selling Products')
plt.ylabel('Quantity Sold')
plt.show()

print("\nConclusion:")
print(f"The top-selling product is: {top_products.idxmax()} with {top_products.max()} items sold.")
print(f"The highest sales category is: {sales_by_category.idxmax()} with a total sale of {sales_by_category.max()}.")
