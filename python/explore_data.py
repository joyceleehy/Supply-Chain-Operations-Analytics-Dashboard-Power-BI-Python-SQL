import pandas as pd

# Load the dataset (this file uses latin1 encoding, not standard utf-8)
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin1")

# 1. How many rows and columns do we have?
print("Shape (rows, columns):", df.shape)

# 2. What are the column names?
print("\nColumn names:")
print(df.columns.tolist())

# 3. Let's peek at the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 4. Data types and missing values summary
print("\nData info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())
