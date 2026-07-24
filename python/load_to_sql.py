import pandas as pd
import sqlite3

# Load the cleaned data
df = pd.read_csv("cleaned_supply_chain_data.csv")

# Connect to (or create) a SQLite database file
conn = sqlite3.connect("supply_chain.db")

# Write the dataframe into a table called 'orders'
df.to_sql("orders", conn, if_exists="replace", index=False)

# Quick check: count rows in the new table
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")
row_count = cursor.fetchone()[0]
print(f"Table 'orders' created successfully with {row_count} rows.")

# Peek at the first 3 rows to confirm it loaded correctly
cursor.execute("SELECT * FROM orders LIMIT 3")
columns = [description[0] for description in cursor.description]
print("\nColumns in table:")
print(columns)

conn.close()
