from fastapi import FastAPI, Body , Query

app = FastAPI()

##DATA SET
movies = [
    {"id": 1, "movie_name": "Inception", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 2, "movie_name": "RRR", "genre": "Action", "language": "Telugu", "rating": 8},
    {"id": 3, "movie_name": "3 Idiots", "genre": "Comedy", "language": "Hindi", "rating": 9},
    {"id": 4, "movie_name": "Interstellar", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 5, "movie_name": "Pushpa", "genre": "Action", "language": "Telugu", "rating": 7}
]

@app.get('/')
def house():
    return("message : Welcome to Movies Adda")

@app.get('/movies')
def get_movies():
    return movies

@app.get("/movies/filter")
def filter_movies(
    genre: str = Query(None),
    language: str = Query(None),
    rating: int = Query(None)
):
    result = []
    for movie in movies:
        if((genre is None or movie["genre"] == genre) and
           (language is None or movie["language"] == language) and
           (rating is None or movie["rating"] >= rating )):
            
            result.append(movie)
    return result

@app.get('/movies/{id}')
def get_movie(id : int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return("No matches found")

@app.post("/movies")
def add_movie(movie: dict = Body(...)):
    movies.append(movie)
    return("Movie added sucessfully!")

@app.put("/movies/{id}")
def update_movie(id : int , updated_movie: dict = Body(...)):
    for movie in movies:
        if movie["id"] == id:
            movie.update(updated_movie)
            return("Updated sucessfully")
    return("Erro 404 Not found")

@app.delete("/movies/{id}")
def delete_movie(id:int):
    for movie in movies:
        if movie ["id"] == id:
            movies.remove(movie)
            return("Deleted Sucessfully")
    return(" Error 404 Movie not found!")
    

    
        

