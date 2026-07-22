import sqlite3
import pandas as pd
from pathlib import Path


def extract_sqlite_data():

    BASE_DIR = Path(__file__).resolve().parents[1]

    db_path = BASE_DIR / "data" / "company.db"

    print("SQLite database:", db_path)

    conn = sqlite3.connect(db_path)

    df = pd.read_sql(
        "SELECT * FROM employees",
        conn
    )

    conn.close()

    print(f"Extracted {len(df)} employees")

    return df