from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import  executor

import os

from dotenv import load_dotenv

from keyboards import kb_client
from pricesearch import price_search

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    mes = (f'Здравсуйте, {message.from_user.first_name}. '
           f'Я помогу вам обменять валюту по лучшим ценнам в вашем городе. '
           f'Какую валюту вы хочете обменять?')
    await bot.send_message(message.from_user.id, mes, reply_markup=kb_client)

@dp.message_handler()
async def asnwer(message : types.Message):
    currency = message.text
    if currency =='Доллары':
        answer = price_search('usd')
    elif currency =='Евро':
        answer = price_search('eur')
    await message.answer(answer)



executor.start_polling(dp, skip_updates=True)
