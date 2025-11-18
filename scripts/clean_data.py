import pandas as pd

def clean_netflix_data(df):
    """
    Clean Netflix dataset:
    - Remove duplicates
    - Fill missing director/cast/country
    - Convert date format
    """
    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing essential fields
    df["director"].fillna("Unknown", inplace=True)
    df["cast"].fillna("Unknown", inplace=True)
    df["country"].fillna("Unknown", inplace=True)

    # Convert date_added to datetime
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    print("✅ Cleaning completed.\n")
    return df


if __name__ == "__main__":
    raw_df = pd.read_csv("../data/netflix.csv")
    cleaned_df = clean_netflix_data(raw_df)
    print(cleaned_df.head())