# 03_pycon_bs4_test.py
import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.pycon.kr/2017/')
html = response.text
soup = bs(html, 'html.parser')

content_list = soup.select('body > div.frontpage > div.onsky > div > div > p > span')

for i in content_list:
    print(i.text)
    