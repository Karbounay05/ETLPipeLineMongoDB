import sqlite3
import pandas as pd

def extract_sqlite_data():

    conn = sqlite3.connect("data/company.db")

    df = pd.read_sql(
        "SELECT * FROM employees",
        conn
    )

    conn.close()

    print(f"Extracted {len(df)} employees")

    return df