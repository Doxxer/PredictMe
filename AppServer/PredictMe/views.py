# Create your views here.
from django.shortcuts import render_to_response
from PredictMe.movies_database import find_movies


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
    return render_to_response('movie.html')