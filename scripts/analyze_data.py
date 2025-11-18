import pandas as pd

def analyze(df):
    """
    Print important insights about the dataset.
    """

    print("\n===== 📊 Dataset Overview =====")
    print("Total rows:", len(df))

    print("\n===== 🎬 Movies vs TV Shows =====")
    print(df["type"].value_counts())

    df["country"].fillna("Unknown", inplace=True)

    print("\n===== 🌎 Top 10 Countries by Content =====")
    print(df["country"].value_counts().head(10))

    print("\n===== 🎭 Top Genres =====")
    print(df["listed_in"].value_counts().head(10))


if __name__ == "__main__":
    df = pd.read_csv("../data/netflix.csv")
    analyze(df)