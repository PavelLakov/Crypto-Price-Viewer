import pandas as pd
import sqlite3
import os

# List of CSV files
csv_files = [
    "Avalanche Historical Data.csv",
    "Bitcoin Historical Data.csv",
    "BNB Historical Data.csv",
    "Cardano Historical Data.csv",
    "Chainlink Historical Data.csv",
    "Dogecoin Historical Data.csv",
    "Ethereum Historical Data.csv",
    "Hedera Historical Data.csv",
    "Litecoin Historical Data.csv"
]

# Folder containing the CSVs
folder_path = "."

# Output database file
db_path = "crypto_data.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Load each CSV into a separate table
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    table_name = file.replace(" Historical Data.csv", "").replace(" ", "_").lower()
    print(f"Importing {file} into table '{table_name}'...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()
print(f"✅ Database created at '{db_path}'")
