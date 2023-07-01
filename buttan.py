from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

meva1 = KeyboardButton('olma')
meva2 = KeyboardButton('anor')

natija = ReplyKeyboardMarkup(resize_keyboard=True).add(meva1,meva2)