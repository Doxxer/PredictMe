import pickle

import imdb

from Web.settings import FAKE_DATA, DUMP_DATA


__author__ = 'doxer'


def find_movies(query):
    if FAKE_DATA:
        pickle_load = pickle.load(open('movies.txt', 'rb'))
        return pickle_load

    if len(query) < 3:
        return []

    db = imdb.IMDb()
    movies = db.search_movie(query)
    for movie in movies:
        movie['extra_data'] = {}
        movie['extra_data']['title'] = movie['long imdb title']

    if DUMP_DATA:
        pickle.dump(movies, open('movies.txt', 'wb'))

    return movies


def get_person_name(movie, job):
    cast = []
    for person in movie[job]:
        cast.append({
            'name': person['long imdb name'],
        })
    return cast


def get_our_rating():
    return 42.5


def get_movie_info(movie_id):
    if FAKE_DATA:
        movie = pickle.load(open('the_matrix.txt', 'rb'))
        return movie

    db = imdb.IMDb()
    movie = db.get_movie(movie_id, info='main')

    cast = []
    for artist in movie['cast']:
        cast.append({
            'name': artist['long imdb name'],
            'role': artist.currentRole['name']
        })

    directors = get_person_name(movie, 'director')

    movie_object = {
        'title': movie['long imdb title'],
        'image': movie['full-size cover url'],
        'director': directors,
        'writer': get_person_name(movie, 'writer'),
        'cast': cast,
        'our_rating': get_our_rating(),
        'imdb_rating': movie['rating'],
        'year': movie['year']
    }

    if DUMP_DATA:
        pickle.dump(movie_object, open('the_matrix.txt', 'wb'))
    return movie_object