from urllib.request import Request, urlopen
import bs4

req = Request('https://lord4.lordfilm.lu/filmy/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'})
webpage = urlopen(req).read()
html = bs4.BeautifulSoup(webpage, 'html.parser')
print(html)
items = html.select('.pagi-nav > .navigation > a')[-1].text
print(items)
#     return items
# import requests
# from bs4 import BeautifulSoup
# import cfscrape
#
# URL = 'https://lord4.lordfilm.lu/filmy/'
# HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
# 'Connection': 'keep-alive',
# 'Cookie': 'PHPSESSID=7sactmqmcta4gtrsqpv47in4s8; __cf_bm=UtSfMxodOi.tgKQDkJXFECAnvx0iJOs8khGJw.vjATw-1665139116-0-AUMmxsQR7Vj2jwN5eZ2AsttBtvogb+RhoNv3dfdsdNJ+ZSIsLeRHlbg/H7VGfDDbutu9LNzuS8ettnIdgJvFckzPPuqlWPLx6xtUdNyAfRVwG/VzLE09mXpJRf9fP8cq6g==',
# 'Host': 'lord4.lordfilm.lu',
# 'Referer': 'https://lord4.lordfilm.lu/filmy/page/1005/',
# 'Sec-Fetch-Dest': 'document',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-Site': 'same-origin',
# 'Sec-Fetch-User': '?1',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
# }
#
# # response = requests.get('http://188.114.99.192:80/filmy/')
# # cookies = response.cookies.get_dict()
# # header = response.headers
# # print(cookies)
# # print(header)
# session = requests.Session()
# session.headers = HEADERS
# r = session.get(URL)
# soup = requests.get(URL, HEADERS)
# print(soup.read())
# if r.status_code == 200:
#     print('yes')
#     print(list(r.content))
# else:
#     print('no')


# def get_html(url, params=None):
#     r = requests.get(url, headers=headers, params=params, cookies=cookies)
#     return r
#
#
# def parse():
#     html = get_html(URL)
#     print(html)
#
#
# print(parse())
# import requests
# import bs4
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# def parse_all_films_page(url, pages):
#     pass
#
# def parse_all_films_link():
#     url = 'https://lord4.lordfilm.lu/filmy/'
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get(url)
#
#     # soup = requests.get(url=url,
#                         # cookies={
#                         #     "__cf_bm": "UtSfMxodOi.tgKQDkJXFECAnvx0iJOs8khGJw.vjATw-1665139116-0-AUMmxsQR7Vj2jwN5eZ2AsttBtvogb+RhoNv3dfdsdNJ+ZSIsLeRHlbg/H7VGfDDbutu9LNzuS8ettnIdgJvFckzPPuqlWPLx6xtUdNyAfRVwG/VzLE09mXpJRf9fP8cq6g==",
#                         #     "PHPSESSID": "7sactmqmcta4gtrsqpv47in4s8"
#                         # },
#
#
#                         # params={
                        #                  }
#                         # )
#     print(soup)
#     time.sleep(3)
#     html = bs4.BeautifulSoup(soup.content, 'html.parser')
#     print(html)
#     items = html.select('.pagi-nav > .navigation > a')
#     print(items)
#     return items
#
# print(parse_all_films_link())