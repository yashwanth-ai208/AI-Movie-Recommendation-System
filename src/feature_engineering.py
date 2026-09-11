import pandas as pd
import ast


def convert_to_list(text):
    """Extract names from JSON-like movie data."""
    try:
        data = ast.literal_eval(text)

        if isinstance(data, list):
            return [item["name"] for item in data if "name" in item]

        return []
    except:
        return []


def extract_cast(text):
    """Extract the first 5 actors."""
    try:
        data = ast.literal_eval(text)

        if isinstance(data, list):
            return [item["name"] for item in data[:5] if "name" in item]

        return []
    except:
        return []


def extract_director(text):
    """Extract the director from crew information."""
    try:
        data = ast.literal_eval(text)

        for item in data:
            if item.get("job") == "Director":
                return [item["name"]]

        return []
    except:
        return []


def create_tags(movies):
    """Create a combined tags column."""

    movies["genres"] = movies["genres"].apply(convert_to_list)
    movies["keywords"] = movies["keywords"].apply(convert_to_list)
    movies["cast"] = movies["cast"].apply(extract_cast)
    movies["crew"] = movies["crew"].apply(extract_director)

    movies["overview"] = movies["overview"].apply(
        lambda x: x.split() if isinstance(x, str) else []
    )

    movies["tags"] = (
        movies["genres"]
        + movies["keywords"]
        + movies["overview"]
        + movies["cast"]
        + movies["crew"]
    )

    movies["tags"] = movies["tags"].apply(
        lambda x: " ".join(x).lower()
    )

    return movies


if __name__ == "__main__":

    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    credits = credits.rename(columns={"movie_id": "id"})
    credits = credits.drop(columns=["title"])

    movies = movies.merge(credits, on="id")

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

    movies = movies.dropna()

    movies = create_tags(movies)

    print("Feature engineering completed successfully!")

    print("\nMovie:", movies.iloc[0]["title"])

    print("\nTags:")
    print(movies.iloc[0]["tags"][:500])