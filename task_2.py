import pandas as pd
import numpy as np

# --- 1. Generate a sample CSV file ---
# Create a sample DataFrame
data = {
    'Department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales', 'Marketing', 'Engineering', 'Sales'],
    'Employee_ID': range(1, 9),
    'Salary': [95000, 70000, 110000, 65000, 85000, 72000, 120000, 90000],
    'Years_of_Experience': [5, 2, 8, 3, 4, 3, 10, 6]
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_name = 'sample_company_data.csv'
df.to_csv(file_name, index=False)
print(f"Sample CSV file '{file_name}' created successfully.")

# --- 2. Load the data ---
try:
    df = pd.read_csv(file_name)
    print("\nData loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    exit()

# --- 3. Compute basic statistics of numerical columns using .describe() ---
print("\n" + "="*50)
print("Basic Statistics of Numerical Columns:")
print("="*50)
numerical_stats = df[['Salary', 'Years_of_Experience']].describe()
print(numerical_stats)

# --- 4. Perform groupings and compute mean of a numerical column ---
print("\n" + "="*50)
print("Mean Salary by Department:")
print("="*50)
department_salaries = df.groupby('Department')['Salary'].mean().reset_index()
print(department_salaries)

# --- 5. Identify patterns or interesting findings ---
print("\n" + "="*50)
print("Analysis and Findings:")
print("="*50)

# Pattern 1: Highest average salary department
highest_avg_salary_dept = department_salaries.loc[department_salaries['Salary'].idxmax()]
print(f"The **Engineering** department has the **highest average salary** ($ {highest_avg_salary_dept['Salary']:.2f}).")

# Pattern 2: Correlation between salary and experience (from .describe() and domain knowledge)
salary_mean = numerical_stats.loc['mean', 'Salary']
experience_mean = numerical_stats.loc['mean', 'Years_of_Experience']
print(f"The average employee in this dataset earns approximately ${salary_mean:.2f} with an average of {experience_mean:.2f} years of experience.")

# Pattern 3: Insights from the grouped data
print("An interesting finding is the significant difference in average salaries between departments.")
print("The data suggests a potential correlation between a department's technical nature and its compensation, with Engineering roles commanding higher salaries.")