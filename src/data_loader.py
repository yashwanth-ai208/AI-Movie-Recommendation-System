import pandas as pd

# Load movie data
movies = pd.read_csv("data/tmdb_5000_movies.csv")

# Load credits data
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Display basic information
print("Movies dataset loaded successfully!")
print("Number of movies:", len(movies))
print("Number of credit records:", len(credits))

print("\nMovie columns:")
print(movies.columns.tolist())

print("\nCredit columns:")
print(credits.columns.tolist())
print("\nFirst 5 movie titles:")
print(movies["title"].head())

print("\nSelected movie features:")
print(movies[["title", "genres", "keywords", "overview"]].head(3))
