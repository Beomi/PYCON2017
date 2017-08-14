# 02_pycon_bs4.py 
import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.pycon.kr/2017/')
html = response.text
soup = bs(html, 'html.parser')

# CSS Selector로 원하는 부분 가져오기(리스트)
title = soup.select('body > div.frontpage > div.onsky > div > div > h1')
# html태그 뺀 텍스트 가져오기
print(title[0].text)