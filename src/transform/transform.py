import pandas as pd

def clean_dataframe(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where all values are missing
    df = df.dropna(how="all")

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Remove extra spaces from text columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    return df