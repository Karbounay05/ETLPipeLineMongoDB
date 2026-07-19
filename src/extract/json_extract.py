import pandas as pd


def extract_json_data(file_path):
    df = pd.read_json(file_path)

    print(f"Extracted {len(df)} records from {file_path}")

    return df