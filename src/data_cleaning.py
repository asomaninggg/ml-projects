import pandas as pd

def clean_salary_data(df):
    "cleans data by dropping values and removing duplicates"

    df = df.dropna()
    df = df.drop_duplicates()
    return df    
    
def check_missing_duplicates(df):
    "prints count for missing values and duplicates"

    print("Missing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    