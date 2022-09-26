import json

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Create your views here.

from django.core import serializers
from django.http import HttpResponse

# def some_view(request):
#     qs = SomeModel.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')


def index(request):
    try:
        films_year = Film.objects.all().order_by('name', 'year_of_release', 'rating_imdb', 'saw')
        # films_saw = Film.objects.all().order_by('saw', 'rating_imdb', 'year_of_release')
        # collections = Collection.objects.all().order_by('sort')
        # genres = Genre.objects.all()
        # context = [{'name': obj.name} for obj in films_year]
        context = [obj.json_dump_film() for obj in films_year]
        print(context)
        status = 200
        # context = {
        #     'films_year': films_year,
        #     # 'films_saw': films_saw,
        #     # 'collections': collections,
        #     # 'genres': genres,
        # }
        # context = json.dumps({'data': context})
        return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
    except TypeError:
        status = 500
        context = {
            'message': 'Error'
        }
        return HttpResponse(json.dumps({'data': context}), content_type='application/json')
    # return JsonResponse(status=status, json.dumps({'data': context}))


def film(request, film=None):
    film=film
    try:
        film = Film.objects.filter(id=film)
        context = [obj.json_dump_film() for obj in film]
        status = 200
        return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
    except TypeError:
        status = 500
        context = {
            'message': 'Error'
        }
        return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


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