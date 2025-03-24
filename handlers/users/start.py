from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum {message.from_user.full_name}.\n\n"
                         "Menga biror matn yuboring (lotin alifbosida yozilgan, "
                         "rasm emas) va men sizga qo'lyozma shaklidagi rasm qaytaraman")
