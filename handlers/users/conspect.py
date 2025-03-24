from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils.misc.functions import row, bogin, Con
from utils.misc.backend import Main
from states.options import chooseOptions
from keyboards.default.paper_types import paperType

@dp.message_handler(state=None)
async def input_text(message: types.Message, state: FSMContext):
    await message.answer("Varoq turini tanlang:", reply_markup=paperType)
    await chooseOptions.paper_type.set()

    await state.update_data(
        {'text': message.text}
    )


@dp.message_handler(state=chooseOptions.paper_type)
async def conspect(message: types.Message, state: FSMContext):
    await message.answer(text="Iltimos, bir oz kutib turing🕓\nKonspekt tayyorlanmoqda🚀", reply_markup=types.ReplyKeyboardRemove())

    data = await state.get_data()
    text = data.get('text')
    typePaper = message.text

    Text = Con(typePaper, text)

    konspekt = Main(typePaper)
    konspekt.write(Text)

    photo = open('data/images/Konspekt.png', 'rb')
    await message.answer_photo(photo, reply_markup=types.ReplyKeyboardRemove())

    await state.finish()
