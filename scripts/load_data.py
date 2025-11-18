import pandas as pd
from pathlib import Path

def load_netflix_data(path="../data/netflix.csv"):
    """
    Load Netflix dataset from CSV file.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    print("✅ Data loaded successfully!")
    print(df.head(), "\n")

    return df


if __name__ == "__main__":
    load_netflix_data()