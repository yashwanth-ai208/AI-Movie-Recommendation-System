import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from feature_engineering import create_tags


def prepare_data():
    # Load datasets
    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    # Rename ID column
    credits = credits.rename(columns={"movie_id": "id"})

    # Remove duplicate title column
    credits = credits.drop(columns=["title"])

    # Merge datasets
    movies = movies.merge(credits, on="id")

    # Select required columns
    movies = movies[
        [
            "title",
            "genres",
            "keywords",
            "overview",
            "cast",
            "crew"
        ]
    ]

    # Remove missing values
    movies = movies.dropna()

    # Create tags
    movies = create_tags(movies)

    return movies


def build_similarity_matrix(movies):
    # Convert tags into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(movies["tags"])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors)

    return similarity


if __name__ == "__main__":

    print("Preparing movie data...")

    movies = prepare_data()

    print("Building similarity matrix...")

    similarity = build_similarity_matrix(movies)

    print("\nRecommendation engine created successfully!")

    print("Number of movies:", len(movies))

    print("Similarity matrix shape:", similarity.shape)

    print("\nExample similarity scores:")
    print(similarity[0][:5])

def recommend_movies(movie_title, movies, similarity, number=5):

    # Find movie index
    movie_index = movies[
        movies["title"].str.lower() == movie_title.lower()
    ].index

    if len(movie_index) == 0:
        print("Movie not found!")
        return

    movie_index = movie_index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended movies:")

    count = 0

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        print(movies.iloc[index]["title"])

        count += 1

        if count == number:
            break


