import pandas as pd

# Load the raw dataset
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin1")

# 1. Drop columns we don't need
columns_to_drop = [
    "Product Description",   # 100% empty
    "Order Zipcode",          # 86% missing, unreliable
    "Customer Email",         # sensitive, not needed for analysis
    "Customer Password"       # sensitive, not needed for analysis
]
df = df.drop(columns=columns_to_drop)

# 2. Convert date columns from text to real datetime
df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])

# 3. Clean up column names: lowercase, spaces to underscores, remove brackets/parentheses
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

# Rename the two awkward date columns to something cleaner
df = df.rename(columns={
    "order_date_dateorders": "order_date",
    "shipping_date_dateorders": "shipping_date"
})

# 4. Quick check before saving
print("Cleaned shape (rows, columns):", df.shape)
print("\nCleaned column names:")
print(df.columns.tolist())

# 5. Save the cleaned version as a new file (never overwrite the raw original)
df.to_csv("cleaned_supply_chain_data.csv", index=False)
print("\nSaved cleaned_supply_chain_data.csv successfully.")