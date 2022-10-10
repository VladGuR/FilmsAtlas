import parse_films.list_films as lf
from .models import Genre
from django.http import HttpResponse
import json

f = ["«'What's done cannot be undone.'»", "«do drugs... do crime.. repeat»",
     "«A mystical meta-musical about the biggest financial fraud in history»", "Режиссер"]
all_genge_list = []


def check_all_genre():
    for film in lf.list_films:
        list_genre = film['genre']
        genre_list = list_genre.split(', ')
        for genre in genre_list:
            all_genge_list.append(genre)

    sort_genre_list = []
    for genre in all_genge_list:
        if genre in sort_genre_list or genre in f:
            continue
        else:
            sort_genre_list.append(genre)

    return sort_genre_list


def genre_update(request):
    if request.method == 'GET':
        try:
            genre_model = Genre.objects.all()
            context = {
                'title': 'genre',
                'content': [obj.name for obj in genre_model] if genre_model else 'Страны не добавлены',
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
                genre_model = Genre.objects.all().order_by('name')
                genre_name = [str(obj.name) for obj in genre_model] if genre_model else 'Жанры не добавлены'
                genre = check_all_genre()
                if genre:
                    for gen in genre:
                        if gen in genre_name:
                            continue
                        else:
                            Genre.objects.create(name=gen)
                    context = {
                        'title': 'genre',
                        'content': genre_name,
                    }
                    status = 200
                    return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')

                else:
                    context = {
                        'title': 'genre',
                        'content': [obj.name for obj in genre_model] if genre_model else 'Жанры не добавлены',
                    }
                    status = 200
                    return HttpResponse(status=status, content=json.dumps({'data': context}),
                                        content_type='application/json')
            else:
                country_model = Genre.objects.all()
                context = {
                    'title': 'genre',
                    'content': [obj.name for obj in country_model] if country_model else 'Страны не добавлены',
                }
                status = 200
                return HttpResponse(status=status, content=json.dumps({'data': context}),
                                    content_type='application/json')
        except TypeError:
            status = 500
            context = {
                'message': 'Error'
            }
            return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')