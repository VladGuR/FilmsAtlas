from urllib.request import Request, urlopen
import bs4
import json
import list_films

URL = 'https://lord4.lordfilm.lu/filmy/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}


def save_film(film):
    if film in list_films.list_films:
        print('Есть!')
    else:
        list_films.list_films.append(film)
        f = open('list_films.py', 'w', encoding='utf-8')
        f.write(f'list_films ={list_films.list_films}')
        f.close()


def check_film(link):
    req = Request(link, headers=HEADERS)
    webpage = urlopen(req).read().decode("utf8")
    html = bs4.BeautifulSoup(webpage, 'html.parser')

    flists = html.select('.full > script')
    for obj in flists:
        try:
            gen = []
            json_obj = json.loads(obj.text)
            desc = json_obj['description']
            name = json_obj['name']
            url_film = json_obj['url']
            img = json_obj['thumbnailUrl']
            upload_date = json_obj['uploadDate']
            date_published = json_obj['datePublished']
            genre = json_obj['genre']
            genre_list = genre.split(', ')
            for obj in genre_list:
                gen.append(obj)
            embed_url = json_obj['embedUrl']
        except:
            continue
    context = {
        'name': name,
        'desc': desc,
        'img': img,
        'url': url_film,
        'upload_date': upload_date,
        'date_published': date_published,
        'genre': gen,
        'embed_url': embed_url,
    }
    save_film(context)
    return context


def check_films(pages):
    films_list = []
    for page in range(1, int(pages)):
        req = Request(URL+'page/'+str(page)+'/', headers=HEADERS)
        webpage = urlopen(req).read()
        html = bs4.BeautifulSoup(webpage, 'html.parser')
        items = html.select('.th-item > a')
        for item in items:
            films_list.append(check_film(item['href']))
        print('page: ', page)

    return films_list


def check_page():
    req = Request(URL, headers=HEADERS)
    webpage = urlopen(req).read()
    html = bs4.BeautifulSoup(webpage, 'html.parser')
    # print(html)
    items = html.select('.pagi-nav > .navigation > a')[-1].text
    # print(items)
    response = check_films(items)
    return response


s = check_page()
print(s)
print(len(s))

# f = open('list_films.py', 'a')
# for obj in s:
#     f.write(str(obj) + '\n')
# f.write(']')
# f.close()