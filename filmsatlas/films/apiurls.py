from django.urls import re_path, include
import films.apiviews as films
import films.country as country

app_name = 'films'

urlpatterns = [
    re_path('$', films.index, name='index'),
    re_path('genres/$', films.genres, name='genres'),
    re_path('genre/(?P<genre>\d+)/$', films.genre, name='genre'),
    re_path('genre/add/$', films.genre_add, name='genre_add'),
    re_path('genre/(?P<genre>\d+)/delete/$', films.genre_delete, name='genre_delete'),
    re_path('sort-year/(?P<year>.*\s*)/$', films.year, name='year'),
    re_path('sort-country/(?P<country>.*\s*)/$', films.country, name='country'),
    re_path('collections/$', films.collections, name='collections'),
    re_path('collection/(?P<collection>.*\s*)/$', films.collection, name='collection'),
    re_path('film/(?P<film>\d+)/$', films.film, name='film'),
    # re_path('films/add/$', films.films_add, name='films_add'),
    re_path('film/(?P<film>\d+)/delete/$', films.film_delete, name='film_delete'),
    re_path('search/(?P<search>.*\s*)/$', films.search, name='search'),
    re_path('country/update/$', country.country_update, name='country_update')
]