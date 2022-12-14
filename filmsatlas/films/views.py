from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Create your views here.


def index(request):
    films_year = Film.objects.all().order_by('year', 'rating_imdb', 'saw')
    films_saw = Film.objects.all().order_by('saw', 'rating_imdb', 'year')
    collections = Collection.all().order_by('sort')
    genres = Genre.objects.all()
    context = {
        'films_year': films_year,
        'films_saw': films_saw,
        'collections': collections,
    }
    return render(request, '/films/Atlas_main_page.html', context)
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