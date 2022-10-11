from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Create your views here.
from django.core.paginator import Paginator


def index(request):
    if request.method == 'GET':
        films = Film.objects.all().order_by('year_of_release', 'rating_imdb', 'saw').reverse()
        # films = [obj.check_film() for obj in films_year]
        films_page = Paginator(films, 50)
        pages = films_page.page(1)
        films = pages.object_list
        films_collection = Collection.objects.all()[:10]
        genres = Genre.objects.all()
        context = {
            'films': films,
            'films_collection': films_collection,
            'genres': genres,
            'films_page': films_page,
        }
        return render(request, 'films/index.html', context)


def films_page(request, page=None):
    page = int(page)
    if request.method == 'GET':
        films = Film.objects.all().order_by('year_of_release', 'rating_imdb', 'saw').reverse()
        # films = [obj.check_film() for obj in films_year]
        films_page = Paginator(films, 50)
        films_collection = Collection.objects.all()[:10]
        pages = films_page.page(page)
        print(films_page.count)
        print(films_page.num_pages)
        films = pages.object_list
        genres = Genre.objects.all()
        context = {
            'films': films,
            'films_collection': films_collection,
            'genres': genres,
            'films_page': films_page,
            'page': page
        }
        return render(request, 'films/index.html', context)


def film(request, film=None):
    film = film
    if request.method == 'GET':
        films = Film.objects.get(name=film)
        context = films.check_film()
    return render(request, 'films/film.html', context)


def genres(request):
    pass
    # genres_all = Genre.objects.all().order_by('name')
    # genres =


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