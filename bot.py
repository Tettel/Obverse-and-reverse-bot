# coding=utf8
from pyrogram import Client
from pyrogram import Filters
import random
import re

app = Client(
    session_name="my_account",
    api_id=YOUR ID,
    api_hash="YOUR HASH"
)

app = Client("my_account")

app.start() #запускаем клиент

@app.on_message(Filters.regex("кинь (монетку|монету)", re.I)) #регулярное выражение(можно изменить на свою фразу)
def my_handler(client, message):
    ch_id = message.chat.id #Переменные для облегчения работы
    us_id = message.from_user.id
    ms_id = message.message_id
    ran_num = random.randint(1, 2) #Сам рандомайзер(можно вставить свои значения)
    if us_id == 377703807: #ВСТАВИТЬ СВОЙ ID
        pass #Создано для того, чтобы бот не отвечал на свои сообщения
    else:
        if ran_num == 1: #Если вышло число 1, выпадает решка.
            app.send_message(chat_id=ch_id, text=f'<b>Выпала:</b> <b>Решка</b>', reply_to_message_id=ms_id, parse_mode='HTML')
        else: #Если другое число - орел
            app.send_message(chat_id=ch_id, text=f'<b>Выпал:</b> <b>Орел</b>', reply_to_message_id=ms_id, parse_mode='HTML')

app.idle()
