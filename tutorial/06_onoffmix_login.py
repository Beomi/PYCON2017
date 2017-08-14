import requests
from bs4 import BeautifulSoup as bs

# 세션 만들기(로그인정보 유지)
s = requests.Session()
# 크롬 브라우저라고 서버에 알려주기
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
# `post`방식으로 로그인하기
# email / pw / proc는 input태그의 name 속성값
login = s.post('https://onoffmix.com/account/login', data={
    'email': '이메일',
    'pw': '패스워드',
    'proc': 'login'
})
# 신청 이벤트 페이지 가져오기
html = s.get('http://onoffmix.com/account/event')
soup = bs(html.text, 'html.parser')

# 신청 이벤트 목록 만들기
event_list = soup.select('#eventListHolder > div > ul > li.title > a')
for event in event_list:
    print(event.text)
