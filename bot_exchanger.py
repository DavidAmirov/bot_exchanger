from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import  executor

import os

from dotenv import load_dotenv

from client_messages import START_MESSAGE
from pricesearch import price_search
from keyboards import ikb

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text=START_MESSAGE, reply_markup= ikb)

@dp.callback_query_handler()
async def cl_answer(callback: types.CallbackQuery):
    data = callback.data
    answer = price_search(data)
    await callback.message.answer(text=answer, reply_markup= ikb)

executor.start_polling(dp, skip_updates=True)
