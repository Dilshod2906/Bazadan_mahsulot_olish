import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from buttan import natija
import sqlite3

logging.basicConfig(level=logging.INFO)

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('salom',reply_markup=natija)
    
    connect = sqlite3.connect("meva.db")
    cursor = connect.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS mevalar (
        nomi VARCHAR(30),
        narxi NUMERIC NOT NULL,
        miqdori INTEGER  
        )""")
    
    connect.commit()
    
    cursor.execute(""" INSERT INTO mevalar (nomi,narxi,miqdori) VALUES(
        'olma',20000,2)
        ('anor',40000,1
    )""")

    connect.commit()
 
 
@dp.message_handler()
async def meva(message: types.Message):  
    connect = sqlite3.connect("meva.db")
    cursor = connect.cursor()
    if  message.text == 'olma':
        a = cursor.execute("""SELECT narxi FROM mevalar WHERE nomi = 'olma' """).fetchone()
        balance = str(a[0])
        await message.answer(f"sizning maxsulotingiz narxi: {balance}")
    elif message.text == 'anor':
        b = cursor.execute("""SELECT narxi FROM mevalar WHERE nomi = 'anor' """).fetchone()
        pul = str(b[0])
        await message.answer(f"sizning maxsulotingiz narxi: {pul}")
        print(pul)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)