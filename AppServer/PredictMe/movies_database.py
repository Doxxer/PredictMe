import pickle
import imdb
from Web.settings import FAKE_DATA

__author__ = 'doxer'


def find_movies(query):
    if FAKE_DATA:
        pickle_load = pickle.load(open('the_matrix.txt', 'rb'))
        return pickle_load

    result = []
    if len(query) < 3:
        return result

    db = imdb.IMDb()
    movies = db.search_movie(query)
    for movie in movies:
        movie['extra_data'] = {}
        movie['extra_data']['title'] = movie['long imdb canonical title']

    pickle.dump(movies, open('the_matrix.txt', 'wb'))
    return movies