import requests
import telegram
import time
from bs4 import BeautifulSoup as bs

bot = telegram.Bot(token='')
chat_id = bot.getUpdates()[-1].message.chat.id

links = []

while True:
    r = requests.get('https://www.pycon.kr/2017/program/tutorials/')
    soup = bs(r.text, 'html.parser')
    new_link = soup.select('a')
    if new_link != links:
        bot.sendMessage(chat_id=chat_id, text='https://www.pycon.kr/2017/program/tutorials/')
        links = new_link

    time.sleep(30)