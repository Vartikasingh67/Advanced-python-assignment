import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Age': [25, 35, 45, np.nan, 30, 50, 40, 28],
    'Tenure': [1, 12, 24, 6, 36, 48, 3, 18],
    'MonthlyCharges': [50, 70, 90, 60, 80, 100, 55, 65],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Display dataset
print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nCleaned Dataset:")
print(df)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn count
print("\nChurn Count:")
print(df['Churn'].value_counts())

# Average monthly charges
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Visualize churn
df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.show()

# Correlation using NumPy and Pandas
print("\nCorrelation:")
print(df[['Age', 'Tenure', 'MonthlyCharges']].corr())
