from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Create your views here.


def index(request):
    films = Film.objects.all().order_by('year_of_release', 'rating_imdb', 'saw')[:50]
    # films = [obj.check_film() for obj in films_year]
    films_collection = Collection.objects.all()[:10]
    genres = Genre.objects.all()
    context = {
        'films': films,
        'films_collection': films_collection,
        'genres': genres,
    }
    return render(request, 'films/index.html', context)


def films_page(request, page):
    pass


def film(request, film=None):
    pass


def genres(request):
    pass


def genre(request, genre=None):
    pass


def year(request, year=None):
    pass


def country(request, country=None):
    pass


def collections(request):
    pass


def collection(request, collection=None):
    pass


def search(request, search=None):
    pass