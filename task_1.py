import pandas as pd
import numpy as np
import io

# Create a sample sales dataset as a string
data = """OrderID,Product,Category,Sales,Date
1001,Laptop,Electronics,1200.50,2023-01-05
1002,Desk,Furniture,250.75,2023-01-06
1003,Smartphone,,800.00,2023-01-07
1004,Chair,Furniture,NaN,2023-01-08
1005,Monitor,Electronics,350.25,2023-01-09
1006,Keyboard,Electronics,NaN,2023-01-10
1007,Book,,35.00,2023-01-11
1008,Pen,Stationery,5.50,2023-01-12
1009,Table,Furniture,300.00,2023-01-13
"""

# Load the data from the string into a pandas DataFrame
df = pd.read_csv(io.StringIO(data))

print("Dataset loaded successfully.")
 
# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Get a summary of the DataFrame's structure, including data types and non-null counts
print("\nDataset structure and missing values:")
df.info()

# Check the exact number of missing values per column
print("\nNumber of missing values per column:")
print(df.isnull().sum())

# Create a copy of the DataFrame to work with for demonstration
df_cleaned = df.copy()

# A) Handling missing values in numerical columns (e.g., 'Sales')
# For numerical data, we can fill missing values with the mean, median, or a specific value.
# We'll use the mean of the 'Sales' column to fill the NaN values.
mean_sales = df_cleaned['Sales'].mean()
df_cleaned['Sales'].fillna(mean_sales, inplace=True)

# B) Handling missing values in categorical columns (e.g., 'Category')
# For categorical data, it's often best to fill missing values with the mode, a placeholder like 'Unknown', or to drop the rows.
# We will drop the rows where 'Category' is missing because it's a critical identifier for the product.
df_cleaned.dropna(subset=['Category'], inplace=True)

# Check the cleaned DataFrame to confirm missing values have been handled
print("\nCleaned Dataset Info:")
df_cleaned.info()

# Display the cleaned DataFrame
print("\nCleaned DataFrame after handling missing values:")
print(df_cleaned)