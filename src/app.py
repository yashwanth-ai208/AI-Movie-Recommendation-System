import streamlit as st

from recommendation_engine import (
    prepare_data,
    build_similarity_matrix
)


# Page settings
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬"
)


# Title
st.title("🎬 AI Movie Recommendation System")

st.write(
    "Enter a movie name and get similar movie recommendations."
)


# Load movie data
@st.cache_data
def load_movies():

    movies = prepare_data()

    similarity = build_similarity_matrix(movies)

    return movies, similarity


movies, similarity = load_movies()


# Movie input
movie_name = st.text_input(
    "Enter a movie name:"
)


# Recommendation button
if st.button("Recommend Movies"):

    if movie_name:

        movie_index = movies[
            movies["title"].str.lower() == movie_name.lower()
        ].index

        if len(movie_index) == 0:

            st.error("Movie not found!")

        else:

            movie_index = movie_index[0]

            similarity_scores = list(
                enumerate(similarity[movie_index])
            )

            similarity_scores = sorted(
                similarity_scores,
                key=lambda x: x[1],
                reverse=True
            )

            st.subheader("🍿 Recommended Movies")

            count = 0
            shown_movies = set()

            for index, score in similarity_scores:

                title = movies.iloc[index]["title"]

                if index == movie_index:
                    continue

                if title in shown_movies:
                    continue

                st.write(f"🎬 {title}")

                shown_movies.add(title)

                count += 1

                if count == 5:
                    break

    else:

        st.warning("Please enter a movie name.")