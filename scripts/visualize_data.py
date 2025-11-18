import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_plots(df):
    """
    Generate charts:
    - Movie vs TV Show count
    - Content added by year
    """

    # Plot 1 — Movies vs TV Shows
    sns.countplot(data=df, x="type")
    plt.title("Movies vs TV Shows")
    plt.tight_layout()
    plt.show()

    # Plot 2 — Content Added Over Time
    df["year_added"] = df["date_added"].dt.year
    df["year_added"].value_counts().sort_index().plot(kind="bar")

    plt.title("Content Added Over Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("../data/netflix.csv")
    show_plots(df)