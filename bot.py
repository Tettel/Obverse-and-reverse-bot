# coding=utf8
from pyrogram import Client
from pyrogram import Filters
import random
import re

app = Client(
    session_name="my_account",
    api_id=<YOUR ID>,
    api_hash="<YOUR HASH>"
)

app = Client("my_account")
app.start() #запускаем клиент

@app.on_message(Filters.regex("кинь (монетку|монету)", re.I) ~Filters.chat(<туть ваш ID>))
def my_handler(client, message):
    ch_id = message.chat.id #Переменные для облегчения работы
    us_id = message.from_user.id
    ms_id = message.message_id
    
    ran_num = random.randint(1, 2) #Сам рандомайзер(можно вставить свои значения)
     if ran_num == 1: #Если вышло число 1, выпадает решка.
         res = '<b>Выпал: орел</b>'
     else: #Если другое число - орел
         res = '<b>Выпала: решка</b>'
     app.send_message(chat_id=ch_id, text=f'<b>Выпал:</b>' + res, 
                      reply_to_message_id=ms_id, parse_mode='HTML')

app.idle()
