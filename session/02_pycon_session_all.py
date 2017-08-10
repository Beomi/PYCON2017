import requests
from bs4 import BeautifulSoup as bs

# Get방식으로 소스를 가져옵니다.
req = requests.get('https://www.pycon.kr/2017/program/list/')
# 헤더부분이 아닌 HTTP의 Body(Text)를 가져옵니다.
html = req.text
# HTML을 파이썬이 이해하는 Soup 객체로 파싱합니다.
soup = bs(html, 'html.parser')
# CSS Selector를 통해 내용물을 모두 선택합니다.(iterable)
session_list = soup.select('div > div.col-md-9.content > ul > li > a')

for session in session_list:
    # HTML DOM객체의 내용물(text)만 봅니다.
    print(session.text)
