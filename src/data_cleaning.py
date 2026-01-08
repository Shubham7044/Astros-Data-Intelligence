import numpy as np

def clean_data(df):
    df = df.copy()

    # Replace blank strings with NaN
    df = df.replace(" ", np.nan)

    # Fill categorical columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Fill numerical columns
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].median())

    # Remove duplicates
    df = df.drop_duplicates()

    return df
