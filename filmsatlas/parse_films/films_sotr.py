import list_films as lf

f = ["«'What's done cannot be undone.'»", "«do drugs... do crime.. repeat»",
     "«A mystical meta-musical about the biggest financial fraud in history»", "Режиссер"]

def check_all_genre():
    all_genge_list = []
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


def check_all_name():
    all_name = []
    for film in lf.list_films:
        list_name = film['name']
        all_name.append(list_name)

    return all_name


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
        list_date = date[-5:-1]
        list_embed_url = film['embed_url']
        context = {
            'name': list_name,
            'desc': list_desc,
            'genre': genre_film,
            'url': list_url,
            'img': list_img,
            'date': list_date,
            'embed_url': list_embed_url,
        }
        all_films_info.append(context)
    return all_films_info

