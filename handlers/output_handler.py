import aiogram
from aiogram.dispatcher.filters import Text, CommandStart

from databases.postgresql_db import *
from keyboards.reply_markup import *
from states import *


# Очікую команди початку навчання від користувача
async def menu(message: aiogram.types.Message):
    await message.answer(f'{message.from_user.first_name} оберіть варіант відповіді', reply_markup=menu_kb)
    create_user_table(message.from_user.id)
    await OutputStates.study_start.set()


# Виводжу записані слова для навчання
async def study_start(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    await get_words(message.from_user.id, message)


def register_output_handlers(dp: aiogram.Dispatcher):
    dp.register_message_handler(menu, CommandStart() | Text(equals='Меню'), state='*')
    dp.register_message_handler(study_start, Text(equals='Навчання'), state='*')
