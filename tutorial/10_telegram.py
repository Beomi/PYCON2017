# 10_telegram.py
import requests
from bs4 import BeautifulSoup as bs
import telegram

bot = telegram.Bot(
	token=''
	)

chat_id = bot.getUpdates()[-1].message.chat.id

response = requests.get('https://www.pycon.kr/2017/program/speaker/')
html = response.text
soup = bs(html, 'html.parser')

content_list = soup.select('div.col-md-9.content > ul > li > div > h4 > a')

for i in content_list:
    bot.sendMessage(chat_id=chat_id, text=i.text)
