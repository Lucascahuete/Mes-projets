import logging
import os
import json
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")
class Movie:
    def __init__(self, titre: str):
        self.titre = titre.title()
    
    def __str__(self):
        return self.titre
    
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open (DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()
        if self.titre not in movies:
            movies.append(self.titre)
            self._write_movies(movies)
            return True
        else:
           logging.warning(f"{self.titre} est deja présent dans la liste")
           return False
    
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.titre in movies:
            movies.remove(self.titre)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.titre} n'est pas dans la liste")
            return False

def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies
if __name__ == "__main__":
    print(get_movies())