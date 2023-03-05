from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Доллары')
b2 = KeyboardButton('Евро')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2)