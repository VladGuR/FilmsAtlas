import json
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Create your views here.
from .forms import CreateGenre
from django.core import serializers
from django.http import HttpResponse

# def some_view(request):
#     qs = SomeModel.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')


def index(request):
    if request.method == 'GET':
        try:
            films= Film.objects.all().order_by('name', 'year_of_release', 'rating_imdb', 'saw')
            # films_saw = Film.objects.all().order_by('saw', 'rating_imdb', 'year_of_release')
            # collections = Collection.objects.all().order_by('sort')
            # genres = Genre.objects.all()
            # context = [{'name': obj.name} for obj in films_year]
            context = {'title': 'index',
                       'content': [obj.json_dump_film() for obj in films]}
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
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
    # return JsonResponse(status=status, json.dumps({'data': context}))


def film(request, film=None):
    if request.method == 'GET':
        film=film
        try:
            film = Film.objects.filter(id=film)
            context = {'title': 'film',
                       'content': [obj.json_dump_film() for obj in film],}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


def film_add(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', False)
            form = CreateGenre(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                films = Film.objects.all()
                context = {'title': 'film',
                           'content': [obj.json_dump_film(quantity=True) for obj in films], }
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
            else:
                context = {'title': 'film',
                           'content': 'Ошибка в данных'}
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}),
                                    content_type='application/json')
        except TypeError:
            status = 501
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')


def film_delete(request, film=None):
    if request.method == 'GET':
        film=film
        try:
            film = Film.objects.filter(id=film)
            if film:
                film.delete()
            films = Film.objects.all()
            context = {'title': 'genres',
                       'content': [obj.json_dump_film(quantity=True) for obj in films] if genres else "Жанра нету"}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 501
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')


def genres(request):
    if request.method == 'GET':
        try:
            genres = Genre.objects.all()
            context = {'title': 'genres',
                       'content': [obj.json_dump_genre(quantity=True) for obj in genres],}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


def genre_add(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', False)
            form = CreateGenre(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                genres = Genre.objects.all()
                context = {'title': 'genres',
                           'content': [obj.json_dump_genre(quantity=True) for obj in genres], }
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
            else:
                context = {'title': 'genres',
                           'content': 'Ошибка в данных'}
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}),
                                    content_type='application/json')
        except TypeError:
            status = 501
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')


def genre(request, genre=None):
    if request.method == 'GET':
        genre=genre
        try:
            film = Genre.objects.filter(id=genre)
            if film:
                context = {'title': 'genre',
                           'content': [obj.json_dump_genre(quantity=False) for obj in film] if genre else "Жанра нету"}
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
            else:
                context = {'title': 'genre',
                           'content': "Жанра нету"}
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


def genre_delete(request, genre=None):
    if request.method == 'GET':
        genre=genre
        try:
            genre = Genre.objects.filter(id=genre)
            if genre:
                genre.delete()
            genres = Genre.objects.all()
            context = {'title': 'genres',
                       'content': [obj.json_dump_genre(quantity=True) for obj in genres] if genres else "Жанра нету"}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 501
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')


def year(request, year=None):
    if request.method == 'GET':
        year = year
        try:
            films = Film.objects.filter(year_of_release=year).order_by('year_of_release')
            context = {'title': 'sort year_of_release',
                       'content': [obj.json_dump_film() for obj in films]}
            status = 200
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')


def country(request, country=None):
    if request.method == 'GET':
        country = country
        try:
            country = CountryFilm.objects.filter(country=country).order_by('saw', 'rating_imdb', 'year_of_release')
            context = {'title': 'Country',
                       'content': [obj.json_dump_country() for obj in country]}
            status = 200
            return HttpResponse(status=status, context=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), context_type='application/json')


def collections(request):
    if request.method == 'GET':
        try:
            collections = Collection.objects.all()
            context = {'title': 'Collections',
                       'content': [obj.json_dump_collections(quantity=True) for obj in collections]}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


def collection(request, collection=None):
    if request.method == 'GET':
        collection = collection
        try:
            collection = Collection.objects.filter(id=collection)
            context = {'title': 'Collection',
                       'content': [obj.json_dump_collections(quantity=False) for obj in collection]}
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error',
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')


def search(request, search=None):
    pass