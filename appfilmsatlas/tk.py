import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import requests
import re
import json
import sys

http_site = 'http://localhost:8001/films/api/'
# http_all_categories = '/categories&json'
# http_get_categories = '/categoryList&json&path='
# http_all_special_product = '/specialProduct&json'
# http_logo = 'https://test-mebel/image/catalog/v2_v2_v2.png'
# im = Image.open('logo.png').convert('RGBA')
# print(http_site+http_all_categories)

# def replase_name(name):
#     name1 = re.sub(r'(?i)&amp;(?i)', '&', name)
#     name = re.sub(r'(?i)&quot;(?i)', '"', name1)
#     return name
#

def response_api(http_start=None, http_end=None, id=None):
    if http_start and http_end and id:
        response_API = requests.get(http_start + http_end + id)
        return response_API.text
    elif http_start and http_end:
        response_API = requests.get(http_start + http_end)
        return response_API.text
    elif http_start:
        response_API = requests.get(http_start)
        return response_API.text

# def response_api(http_start=None, http_end=None, id=None):
#     if http_start and http_end and id:
#         response_API = requests.get(http_start + http_end + id)
#         return response_API.text
#     elif http_start and http_end:
#         response_API = requests.get(http_start + http_end)
#         return response_API.text
#

def all_films(frame_cont):
    frame_cont = frame_cont
    all_films_text = response_api(http_site)
    print(all_films_text)
    all_films_text = json.loads(all_films_text)
    print(all_films_text)
    all_films_text = all_films_text['data']
    print(all_films_text)
    for obj in all_films_text:
        frame_cont_film = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
        frame_cont_film.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        text_film = f'{obj["name"]}'
        tk.Label(frame_cont, text=text_film, justify=tk.LEFT, font='arial 12', width=15, background='#aaa').pack()

# def all_categories(frame_cont):
#     frame_cont = frame_cont
#     all_categories_text = response_api(http_site, http_all_categories)
#     all_categories = json.loads(all_categories_text)
#     all_categories = all_categories['shop_categories']
#     list_categories_id = list(map(lambda x: dict(x)['category_id'], all_categories))
#     list_categories_name = list(map(lambda x: dict(x)['name'], all_categories))
#     if len(list_categories_name) == len(list_categories_id):
#         for x in range(len(list_categories_id)):
#             tex = f'{list_categories_name[x]}'
#             tk.Label(frame_cont, text=tex, justify=tk.LEFT, font='arial 12', width=35, background='#aaa').pack()

# def loadImage():
#     try:
#         img = Image.open("logo.png").convert('RGBA')
#         print('good')
#         return img
#     except IOError:
#         print("Возникла ошибка во время открытия изображения!")
#         sys.exit(1)

def category(window):
    frame_title = tk.Frame(relief=tk.RAISED,)
    frame_title.pack(side=tk.TOP)
    title_cat = 'Фильмы'
    window.title('FilmsAtlas')
    # im = Image.open("logo.png").convert('RGBA').resize((70, 50))
    # img = ImageTk.PhotoImage(im)
    # title_logo = tk.Label(frame_title, image=img, text='none')
    # title_logo.image = img
    # title_logo.pack(side=tk.LEFT)
    frame_cont = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
    frame_cont.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    title_text = tk.Label(frame_title, text='FilmsAtlas', width=10, height=1, foreground='#000', font='Bold 25')
    title_text.pack(side=tk.RIGHT)
    frame_cont = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
    frame_cont.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
    # button_category = tk.Button(compound='center', text='Фильмы')
    # button_category.pack(side=tk.LEFT)
    cat = tk.Label(frame_cont, text=title_cat, font='arial 14', width=25, height=1)
    cat.pack()
    all_films(frame_cont)


if __name__ == '__main__':
    window = tk.Tk()
    category(window)
    window.mainloop()