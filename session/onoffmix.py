import requests
from bs4 import BeautifulSoup as bs


def main():
    with requests.Session() as s:
        # Login
        s.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        login = s.post('https://onoffmix.com/account/login', data={
            'email': 'usermail@gmail.com',
            'pw': 'mypassword1234',
            'proc': 'login'
        })
        # 신청 이벤트 페이지 가져오기
        html = s.get('http://onoffmix.com/account/event')
        soup = bs(html.text, 'html.parser')

        # 신청 이벤트 목록 만들기
        event_list = soup.select('#eventListHolder > div > ul > li.title > a')
        for event in event_list:
            print(event.text)


if __name__ == '__main__':
    main()
