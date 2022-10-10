import json
from .models import Film, LinkFilm, GenreFilm, Genre
from django.http import HttpResponse
import parse_films.list_films as lf


def check_all_info_films():
    all_films_info = []
    for film in lf.list_films:
        name = film['name']
        list_name = name.split(' (')[0]
        list_desc = film['desc']
        list_genre = film['genre']
        genre_list = list_genre.split(', ')
        genre_film = []
        for genre in genre_list:
            genre_film.append(genre)
        list_url = film['url']
        list_img = film['img']
        date = film['name']
        list_date = date.split('(')[1][0:4]
        list_embed_url = film['embed_url']
        context = {
            'name': list_name,
            'desc': list_desc,
            'genre': genre_film,
            'url': list_url,
            'img': list_img,
            'date': list_date+'-01-01',
            'embed_url': list_embed_url,
        }
        all_films_info.append(context)
    return all_films_info


def films_update(request):
    # pass
    if request.method == 'GET':
        try:
            films_model = Film.objects.all()
            context = {
                'title': 'films',
                'content': [obj.json_dump_film() for obj in films_model] if films_model else 'Страны не добавлены',
            }
            status = 200
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
    if request.method == 'POST':
        try:
            if request.POST['action'] == 'add':
                films_model = Film.objects.all().order_by('name')
                films_name = [str(obj.name) for obj in films_model] if films_model else 'Фильмы не добавлены'
                films_list = check_all_info_films()
                if films_list:
                    for film in films_list:
                        if film['name'] in films_name:
                            continue
                        else:
                            film_add = Film.objects.create(name=film['name'], description=film['desc'],
                                                           year_of_release=film['date'], image=film['img'])
                            if film['embed_url']:
                                LinkFilm.objects.create(name=film_add, link_film=film['embed_url'])
                            if film['genre']:
                                genre = GenreFilm.objects.all()
                                genre_name = [str(obj.name) for obj in genre]
                                for obj in film['genre']:
                                    if obj in genre_name:
                                        gen = GenreFilm.objects.filter(name=obj)
                                        GenreFilm.objects.create(genre=gen, film=film_add)
                                    else:
                                        genre_add = Genre.objects.create(name=obj)
                                        GenreFilm.objects.create(genre=genre_add, film=film_add)

                    films_model = Film.objects.all()
                    context = {
                        'title': 'films',
                        'content': [obj.json_dump_film() for obj in
                                    films_model] if films_model else 'Фильмы не добавлены',
                    }
                    status = 200
                    return HttpResponse(status=status, content=json.dumps({'data': context}),
                                        content_type='application/json')
                else:
                    status = 500
                    context = {
                        'message': 'Not list Error'
                    }
                    return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')