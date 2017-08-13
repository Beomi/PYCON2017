import requests
import telegram
import time

bot = telegram.Bot(token='')
chat_id = bot.getUpdates()[-1].message.chat.id

while True:
    f = open('html.html', 'w+')

    r = requests.get('https://www.pycon.kr/2017/program/tutorials/')

    if r.text != f.read():
        bot.sendMessage(chat_id=chat_id, text='파이콘 사이트가 뭔가 바뀌었어요! https://www.pycon.kr/2017/program/tutorials/')

    f.write(r.text)

    f.close()

    time.sleep(30)

