import streamlit as st
import requests

BASE_URL = "https://movie-explorer-3-0.onrender.com"

st.title("🎬 Movie Explorer App")

menu = st.sidebar.selectbox("Menu", [
    "View Movies",
    "Search Movies",
    "Add Movie",
    "Update Movie",
    "Delete Movie"
])

# VIEW
if menu == "View Movies":
    if st.button("Load Movies"):
        try:
            res = requests.get(f"{BASE_URL}/movies")
            movies_data = res.json()
            if movies_data:
                st.markdown("---")
                cols = st.columns(3)
                for idx, movie in enumerate(movies_data):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div style="background-color: #1f1f1f; padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                            <h4 style="color: #FFD700; margin-top: 0;">{movie.get('movie_name', 'N/A')}</h4>
                            <p style="color: #999; margin: 5px 0;"><b>ID:</b> {movie.get('id', 'N/A')}</p>
                            <p style="color: #999; margin: 5px 0;"><b>Genre:</b> {movie.get('genre', 'N/A')}</p>
                            <p style="color: #999; margin: 5px 0;"><b>Language:</b> {movie.get('language', 'N/A')}</p>
                            <p style="color: #FFD700; margin: 5px 0; font-size: 16px;"><b>⭐ Rating:</b> {movie.get('rating', 'N/A')}/10</p>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("No movies found")
        except Exception as e:
            st.error(f"Error loading movies: {e}")

# SEARCH
elif menu == "Search Movies":
    genre = st.selectbox("Genre", ["Horror", "Action", "Comedy", "Drama", "Sci-Fi"])
    language = st.selectbox("Language", ["", "English", "Hindi", "Telugu"])
    rating = st.number_input("Min Rating", 1, 10)

    if st.button("Search"):
        try:
            params = {}
            if genre:
                params["genre"] = genre
            if language:
                params["language"] = language
            if rating:
                params["rating"] = rating

            res = requests.get(f"{BASE_URL}/movies/filter", params=params)
            movies_data = res.json()
            if movies_data:
                st.markdown("---")
                cols = st.columns(3)
                for idx, movie in enumerate(movies_data):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div style="background-color: #1f1f1f; padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                            <h4 style="color: #FFD700; margin-top: 0;">{movie.get('movie_name', 'N/A')}</h4>
                            <p style="color: #999; margin: 5px 0;"><b>ID:</b> {movie.get('id', 'N/A')}</p>
                            <p style="color: #999; margin: 5px 0;"><b>Genre:</b> {movie.get('genre', 'N/A')}</p>
                            <p style="color: #999; margin: 5px 0;"><b>Language:</b> {movie.get('language', 'N/A')}</p>
                            <p style="color: #FFD700; margin: 5px 0; font-size: 16px;"><b>⭐ Rating:</b> {movie.get('rating', 'N/A')}/10</p>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("No movies found matching your criteria")
        except Exception as e:
            st.error(f"Error searching movies: {e}")

# ADD
elif menu == "Add Movie":
    id = st.number_input("ID", min_value=0, step=1, format="%d")
    name = st.text_input("Movie Name")
    genre = st.selectbox("Genre", ["Action", "Comedy", "Drama", "Sci-Fi","Horror"])
    language = st.selectbox("Language", ["English", "Hindi", "Telugu"])
    rating = st.slider("Rating", 1, 10)

    if st.button("Add"):
        data = {
            "id": id,
            "movie_name": name,
            "genre": genre,
            "language": language,
            "rating": rating
        }
        res = requests.post(f"{BASE_URL}/movies", json=data)
        st.success(res.json())

# UPDATE
elif menu == "Update Movie":
    id = st.number_input("Movie ID", min_value=0, step=1, format="%d")
    name = st.text_input("New Name")
    genre = st.selectbox("Genre", ["Action", "Comedy", "Drama", "Sci-Fi"])
    language = st.selectbox("Language", ["English", "Hindi", "Telugu"])
    rating = st.slider("Rating", 1, 10)

    if st.button("Update"):
        data = {
            "movie_name": name,
            "genre": genre,
            "language": language,
            "rating": rating
        }
        res = requests.put(f"{BASE_URL}/movies/{id}", json=data)
        st.success(res.json())

# DELETE
elif menu == "Delete Movie":
    id = st.number_input("Movie ID", min_value=0, step=1, format="%d")

    if st.button("Delete"):
        res = requests.delete(f"{BASE_URL}/movies/{id}")
        st.warning(res.json())