from django.shortcuts import render_to_response

from PredictMe.movies_info import find_movies, get_movie_info


def index(request):
    return render_to_response('index.html')


def search(request, query):
    """

    :type query: str
    """
    movies = find_movies(query)
    return render_to_response('search.html', {'movies': movies})


def movie(request, id):
    """

    :type id: str
    """
    movie = get_movie_info(id)
    return render_to_response('movie.html', {'movie': movie})