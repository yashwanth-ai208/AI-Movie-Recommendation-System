import pandas as pd


def load_and_merge_data():
    # Load datasets
    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    # Rename movie_id so both datasets can be merged
    credits = credits.rename(columns={"movie_id": "id"})

    # Remove duplicate title column from credits
    credits = credits.drop(columns=["title"])

    # Merge both datasets
    movies = movies.merge(credits, on="id")

    return movies


def select_features(movies):
    # Select only the columns needed for recommendation
    features = [
        "title",
        "genres",
        "keywords",
        "overview",
        "cast",
        "crew"
    ]

    movies = movies[features]

    # Remove movies with missing values
    movies = movies.dropna()

    return movies


if __name__ == "__main__":
    movies = load_and_merge_data()
    movies = select_features(movies)

    print("Preprocessing completed successfully!")
    print("Number of movies:", len(movies))

    print("\nSelected columns:")
    print(movies.columns.tolist())

    print("\nFirst 3 movies:")
    print(movies.head(3))