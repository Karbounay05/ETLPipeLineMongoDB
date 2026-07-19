import sqlite3
import pandas as pd

def extract_sqlite(db_path):

    conn = sqlite3.connect(db_path)

    df = pd.read_sql_query(
        "SELECT * FROM employees",
        conn
    )

    conn.close()

    return df