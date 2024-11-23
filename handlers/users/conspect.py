from aiogram import types

from loader import dp, bot
from utils.misc.functions import row, bogin, Con
from utils.misc.backend import Main


@dp.message_handler(state=None)
async def conspect(message: types.Message):
    await message.answer(text="Iltimos, bir oz kutib turing🕓\nKonspekt tayyorlanmoqda🚀")

    text = message.text
    typePaper = 'katak'

    Text = Con(text)

    konspekt = Main(typePaper+'1')
    konspekt.write(Text)

    photo = open('data/images/Konspekt.png', 'rb')
    await message.answer_photo(photo)
