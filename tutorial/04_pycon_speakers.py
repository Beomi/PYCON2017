# 04_pycon_speakers.py
import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.pycon.kr/2017/program/speaker/')
html = response.text
soup = bs(html, 'html.parser')

content_list = soup.select('div.col-md-9.content > ul > li > div > h4 > a')

for i in content_list:
    print(i.text)
    