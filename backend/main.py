from fastapi import FastAPI, Query, Body

app = FastAPI()

# Dataset
movies = [
    {"id": 1, "movie_name": "Inception", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 2, "movie_name": "RRR", "genre": "Action", "language": "Telugu", "rating": 8},
    {"id": 3, "movie_name": "3 Idiots", "genre": "Comedy", "language": "Hindi", "rating": 9},
    {"id": 4, "movie_name": "Interstellar", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 5, "movie_name": "Pushpa", "genre": "Action", "language": "Telugu", "rating": 7}
]

# Home
@app.get("/")
def home():
    return {"message": "Movie API Running 🚀"}

# Get all movies
@app.get("/movies")
def get_movies():
    return movies

# Get movie by ID
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}

# Filter movies
@app.get("/movies/filter")
def filter_movies(
    genre: str = Query(None),
    language: str = Query(None),
    rating: int = Query(None)
):
    result = movies

    if genre:
        result = [m for m in result if m["genre"] == genre]

    if language:
        result = [m for m in result if m["language"] == language]

    if rating:
        result = [m for m in result if m["rating"] >= rating]

    return result

# Add movie
@app.post("/movies")
def add_movie(movie: dict = Body(...)):
    movies.append(movie)
    return {"message": "Movie added successfully"}

# Update movie
@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated_data: dict = Body(...)):
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(updated_data)
            return {"message": "Movie updated successfully"}
    return {"error": "Movie not found"}

# Delete movie
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted successfully"}
    return {"error": "Movie not found"}