import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWords import checkWord
from cyril_change_latin import to_latin,to_cyrillic

API_TOKEN = '5369609945:AAGWAVwXlNMKgjSgLEQgNMYyRuy9nU-uhjI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):

    await message.reply("Uz-Imlo botga xush kelibsiz")

@dp.message_handler(commands=[ 'help'])
async def send_help(message: types.Message):
    await message.reply("Uz-Imlo bot yordamida xato so'zni topasiz \n Ishlatish uchun so'z yuboring")

@dp.message_handler()
async def uzImloBot(message: types.Message):
    word_msg  = message.text.split()


    for word in word_msg:
        if word.isascii():
            result = checkWord(to_cyrillic(word))
            if result['available']:
                response = f"✅ {to_latin(word.capitalize())}"
            else:
                response = f"❌ {to_latin(word.capitalize())}\n"
                for text in result['matches']:
                    response += f"✅ {to_latin(text.capitalize())}\n"

            await message.answer(response)
        else:
            result = checkWord(word)
            if result['available']:
                response = f"✅ {word.capitalize()}"
            else:
                response = f"❌ {word.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()}\n"

            await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)