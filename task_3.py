import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample DataFrame
data = {
    'Date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=100)),
    'Product_Category': np.random.choice(['Electronics', 'Furniture', 'Clothing'], 100),
    'Sales': np.random.randint(50, 500, 100) + np.arange(100) * 2,
    'Quantity': np.random.randint(1, 10, 100)
}
df = pd.DataFrame(data)

# Save to a CSV and load to simulate the process
df.to_csv('sample_sales_data.csv', index=False)
df = pd.read_csv('sample_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date']) # Ensure Date column is in datetime format

print("Sample data created and loaded successfully.")
print(df.head())

# Group by date to get daily total sales
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='b')
plt.title('Daily Sales Trend Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True)
plt.savefig("sales_linegragh.png")   # save instead of show
plt.close()

# Calculate the average sales for each product category
avg_sales_by_category = df.groupby('Product_Category')['Sales'].mean()

plt.figure(figsize=(8, 5))
avg_sales_by_category.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Average Sales per Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Average Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.savefig("sales_bargragh.png")   # save instead of show
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=10, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distribution of Sales', fontsize=16)
plt.xlabel('Sales Value ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.savefig("sales_histogram.png")   # save instead of show
plt.close()

plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['Sales'], color='teal', alpha=0.7)
plt.title('Relationship Between Sales and Quantity', fontsize=16)
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True)
plt.savefig("sales_scatter.png")   # save instead of show
plt.close()