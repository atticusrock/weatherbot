from config import token
import telepot
import weather

telepot.api.set_proxy('http://3.0.197.245:80')
bot = telepot.Bot(token)

def reply(text, chat_id):
    t = weather.temp(text)
    bot.sendMessage(chat_id, 'В городе {} сейчас {}'.format(text, t))

last_update = 0

while True:
    updates = bot.getUpdates(offset=last_update+1)
    for i in updates:
        if i ['update_id'] > last_update:
            last_update = i ['update_id']
        reply(i['message']['text'], i['message']['chat']['id'])