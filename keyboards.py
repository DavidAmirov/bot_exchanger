from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Доллары',
                           callback_data='usd')
ib2 = InlineKeyboardButton(text='Евро',
                           callback_data='eur')
ib3 = InlineKeyboardButton(text='Фунты',
                           callback_data='gbp')
ib4 = InlineKeyboardButton(text='Юани',
                           callback_data='cny')
ikb.add(ib1, ib2, ib3, ib4)