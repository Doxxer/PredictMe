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


def get_our_rating(year, cast, directors, writers):
    def get_names(dictionary):
        return [person['name'] for person in dictionary][:10]

    cast = get_names(cast)
    directors = get_names(directors)
    writers = get_names(writers)

    print year
    print cast
    print directors
    print writers

    return 42.5


def get_movie_info(movie_id):
    if FAKE_DATA:
        movie = pickle.load(open('the_matrix.txt', 'rb'))
        movie['our_rating'] = get_our_rating(movie['year'], movie['cast'], movie['directors'], movie['writers'])
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
    writers = get_person_name(movie, 'writer')
    year = movie['year']

    movie_object = {
        'title': movie['long imdb title'],
        'image': movie['full-size cover url'],
        'directors': directors,
        'writers': writers,
        'cast': cast,
        'our_rating': get_our_rating(year, cast, directors, writers),
        'imdb_rating': movie['rating'],
        'year': year
    }

    if DUMP_DATA:
        pickle.dump(movie_object, open('the_matrix.txt', 'wb'))
    return movie_object