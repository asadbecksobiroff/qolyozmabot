from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Ushbu bot sizga konspekt qilishga yordam beradi.\n\nBotga ixtiyoriy lotin alifbosida yozilgan matn yuboring. Bot sizga konspekt shaklidagi rasm yuboradi.",
            "\nBuyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


@dp.message_handler(commands=['admin'])
async def admin_help(message: types.Message):
    await message.answer("Admin bilan bog'lanish: @asadbek_sobiroff")