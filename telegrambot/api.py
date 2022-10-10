from bs4 import BeautifulSoup
import requests
import json
key = 'uaORjeBTmxhsb0WAf6q4CoIbjyg8pqpZwsrTNFpGSt4xJ3Ey7Jh2rANYpIUfUF66RtNkMqNox5UDzokkIceQGvTeheSJDXlbRXC5hNDVykP33rISDrdg1dd0Lrs4L788U4hkaWGOW5zfxbQYVPdRUcRtDdny4oKD13U7DoyBMKFTW43ghEIxK6QIM1YPxljuNA8EdSrhNAsk4DONGywiTn5yXtiHlyYsRsMnqh1dwibPdItBateKWMcoeHLemw4A'

import requests

s = requests.Session()

username = 'test_api'

txt = s.post(
    'https://mebel-vsem74.ru/index.php?route=api/login',
    data={'username': username, 'key': key}
).json()

print(txt)
token = txt.get('api_token')

categories_list = []
products_list = []

if token:
    response = requests.get(
        'https://mebel-vsem74.ru/',
        params={'api_token': token}
    ).content
    # print(response)
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup)
    items = soup.select('.product-thumb > .caption')
    print(items)
    products_list = [{'name': obj.select('h4 > a')[0].text, 'price': obj.select('.price > .price-new')[0].text, 'href': obj.select('h4 > a')[0]['href']} for obj in items]
    i=0
    # for obj in items:
    #     print(obj)
    #     price = obj.find('div', {'class': '.prise-new'})
    #     name = obj.find('h4').find('a').text
    #     href = obj.select('h4 > a')['href']
    #     context = {'name': name,
    #                'price': price,
    #                'href': href}
    #     products_list.append(context)
    #     i += 1
    #     print(i)

print(products_list)
print(len(products_list))
