from django.urls import re_path, include
import films.apiviews as apifilms
import films.country as country
import films.genre as genre
import films.films as films

app_name = 'films'

urlpatterns = [
    re_path('$', apifilms.index, name='index'),
    re_path('genres/$', apifilms.genres, name='genres'),
    re_path('genre/(?P<genre>\d+)/$', apifilms.genre, name='genre'),
    re_path('genre/add/$', apifilms.genre_add, name='genre_add'),
    re_path('genre/(?P<genre>\d+)/delete/$', apifilms.genre_delete, name='genre_delete'),
    re_path('sort-year/(?P<year>.*\s*)/$', apifilms.year, name='year'),
    re_path('sort-country/(?P<country>.*\s*)/$', apifilms.country, name='country'),
    re_path('collections/$', apifilms.collections, name='collections'),
    re_path('collection/(?P<collection>.*\s*)/$', apifilms.collection, name='collection'),
    re_path('film/(?P<film>\d+)/$', apifilms.film, name='film'),
    re_path('films/update/$', films.films_update, name='films_update'),
    re_path('film/(?P<film>\d+)/delete/$', apifilms.film_delete, name='film_delete'),
    re_path('search/(?P<search>.*\s*)/$', apifilms.search, name='search'),
    re_path('country/update/$', country.country_update, name='country_update'),
    re_path('genre/update/$', genre.genre_update, name='genre_update'),
]