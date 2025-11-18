from scripts.load_data import load_netflix_data
from scripts.clean_data import clean_netflix_data
from scripts.analyze_data import analyze
from scripts.visualize_data import show_plots

def main():
    print("\n=== 📁 Loading Data ===")
    df = load_netflix_data("data/netflix.csv")

    print("\n=== 🧹 Cleaning Data ===")
    df = clean_netflix_data(df)

    print("\n=== 📊 Analysis ===")
    analyze(df)

    print("\n=== 📈 Visualizations ===")
    show_plots(df)


if __name__ == "__main__":
    main()