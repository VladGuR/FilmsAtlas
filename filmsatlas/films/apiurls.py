from django.urls import re_path, include
import films.apiviews as films

app_name = 'films'

urlpatterns = [
    re_path('$', films.index, name='index'),
    re_path('genres/$', films.genres, name='genres'),
    re_path('genre/(?P<genre>.*\s*)/$', films.genre, name='genre'),
    re_path('genre/(?P<genre>.*\s*)/delete/$', films.genre_delete, name='genre_delete'),
    re_path('sort-year/(?P<year>.*\s*)/$', films.year, name='year'),
    re_path('sort-country/(?P<country>.*\s*)/$', films.country, name='country'),
    re_path('collections/$', films.collections, name='collections'),
    re_path('collection/(?P<collection>.*\s*)/$', films.collection, name='collection'),
    re_path('film/(?P<film>.*\s*)/$', films.film, name='film'),
    re_path('search/(?P<search>.*\s*)/$', films.search, name='search'),
]