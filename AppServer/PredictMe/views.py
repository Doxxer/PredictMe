# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


def search(request, query):
    """

    :type query: str
    """
    data = query
    return render_to_response('search.html', {'data': query})