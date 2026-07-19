import pandas as pd

def extract_csv_data():

    df = pd.read_csv("data/sales.csv")

    print(f"Extracted {len(df)} sales records")

    return df