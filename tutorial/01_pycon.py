# 01_pycon.py
import requests

# GET 방식으로 pycon 홈페이지 가져오기
response = requests.get('https://www.pycon.kr/2017/')
# 가져온 response의 HTML가져오기
print(response.text) # 소스보기랑 같아요

