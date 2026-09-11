# 🎬 AI Movie Recommendation System

An AI-based movie recommendation system that recommends similar movies using content-based filtering and cosine similarity.

## 📌 Project Overview

The AI Movie Recommendation System recommends movies similar to a movie entered by the user.

The system uses movie information from the TMDB 5000 dataset and applies content-based filtering to calculate movie similarity.

A simple and interactive web interface is built using Streamlit.

## ✨ Features

- 🎬 Search for a movie by name
- 🤖 Recommend similar movies
- 🔍 Content-based filtering
- 📊 Cosine similarity for finding similar movies
- ❌ Handles movies that are not found
- 🖥️ Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Git
- GitHub

## 📂 Project Structure

```text
AI-Movie-Recommendation-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── src/
│   ├── app.py
│   ├── data_loader.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── movie_search.py
│   ├── recommendation_analysis.py
│   └── recommendation_engine.py
│
├── tests/
│
├── .gitignore
└── README.md
