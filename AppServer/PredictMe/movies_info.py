import os
import pickle
import urllib

import imdb

from PredictMe.neurnets.neurnets import computeMovieRating
from Web.settings import FAKE_DATA, DUMP_DATA, DEBUG, ACTORS_MAX_COUNT, IMAGES_DIR


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
        return [person['name'] for person in dictionary][:ACTORS_MAX_COUNT]

    cast = get_names(cast)
    directors = get_names(directors)
    writers = get_names(writers)

    rating = round(computeMovieRating(year, cast, writers, directors), 1)

    if DEBUG:
        print year
        print cast
        print directors
        print writers
        print rating

    return rating


def save_image(movie_id, url):
    image_filename = os.path.join(IMAGES_DIR, '{0}.jpg'.format(movie_id))

    if not os.path.isfile(image_filename) and url:
        with open(image_filename, 'wb') as image:
            image.write(urllib.urlopen(url).read())


def get_movie_info(movie_id):
    if FAKE_DATA:
        movie = pickle.load(open('the_matrix.txt', 'rb'))
    else:
        movie = imdb.IMDb().get_movie(movie_id, info='main')
        if DUMP_DATA:
            pickle.dump(movie, open('the_matrix.txt', 'wb'))

    cast = []
    if movie.has_key('cast'):
        for artist in movie['cast']:
            cast.append({
                'name': artist['long imdb name'],
                'role': artist.currentRole
            })

    directors = get_person_name(movie, 'director')
    writers = get_person_name(movie, 'writer')
    year = movie['year']
    save_image(movie_id, movie['full-size cover url'] if movie.has_key('full-size cover url') else None)
    movie_rating = movie['rating'] if movie.has_key('rating') else '---'

    movie_object = {
        'id': movie_id,
        'title': movie['long imdb title'],
        'directors': directors,
        'writers': writers,
        'cast': cast,
        'our_rating': get_our_rating(year, cast, directors, writers),
        'imdb_rating': movie_rating,
        'year': year
    }

    return movie_object