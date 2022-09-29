import json
from .models import Country
from .forms import CreateCountry
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def country_search(url, list_all_country):
    response_page = requests.get(url)
    soup = BeautifulSoup(response_page.content, 'html.parser')
    content = soup.find('div', {'class': 'mw-category-columns'})
    list_all_country_html = content.find_all('div', {'class': 'mw-category-group'})
    for div_country_group in list_all_country_html:
        li_country = div_country_group.find_all('li')
        list_all_country += [country.find('a').text for country in li_country]

def country_loading():
    list_all_country = []
    url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%93%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B0_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    url_2 = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%93%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B0_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4+%D0%A5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%B0%D0%BD%D0%B8%D1%8F#mw-pages'

    country_search(url, list_all_country)
    country_search(url_2, list_all_country)
    return list_all_country

def country_update(request):
    if request.method == 'GET':
        try:
            country_model = Country.objects.all()
            context = {
                'title': 'country',
                'content': [obj.name for obj in country_model] if country_model else 'Страны не добавлены',
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
                country_model = Country.objects.all().order_by('name')
                country_name = [str(obj.name) for obj in country_model] if country_model else 'Страны не добавлены'
                country = country_loading()
                if country.sort() != country_name.sort():
                    for obj in country:
                        Country.objects.create(name=obj)
                    context = {
                        'title': 'country',
                        'content': country_name,
                    }
                    status = 200
                    return HttpResponse(status=status, content=json.dumps({'data': context}), content_type='application/json')
                else:
                    context = {
                        'title': 'country',
                        'content': [obj.name for obj in country_model] if country_model else 'Страны не добавлены',
                    }
                    status = 200
                    return HttpResponse(status=status, content=json.dumps({'data': context}),
                                        content_type='application/json')
            else:
                country_model = Country.objects.all()
                context = {
                    'title': 'country',
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