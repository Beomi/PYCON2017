import requests
from bs4 import BeautifulSoup as bs

req = requests.get('https://www.pycon.kr/2017/program/list/')
html = req.text
soup = bs(html, 'html.parser')

session_list = soup.select('div > div.col-md-9.content > ul > li > a')

for session in session_list:
    print(session.text)
