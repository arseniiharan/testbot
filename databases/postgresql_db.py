import aiogram.types
import psycopg2

from bots_data import HOST, USER, PASSWORD, DB_NAME
from main import bot

connection = psycopg2.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DB_NAME
)

cursor = connection.cursor()

translations = ''


# Створення таблиці юзерів
def create_table():
    connection.autocommit = True

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        user_tg_id varchar(50)
        );"""
    )

    print('Table was successfully created')


# Створення таблиці окремого юзера
def create_user_table(user_id):
    cursor.execute(
        f"""
                CREATE TABLE IF NOT EXISTS user_{user_id}(
                id serial PRIMARY KEY,
                word varchar(100) NOT NULL,
                translation varchar(100) NOT NULL,
                status varchar(10) NOT NULL
                );"""
    )


# Достаю слова из бд
async def get_words(user_id, message):
    connection.autocommit = True
    list_number = 0
    try:
        cursor.execute(
            f"""
            SELECT word FROM user_{user_id};
            """
        )
        words = cursor.fetchone()[s]
        for n in words:
            await message.answer(message.from_user.id, f'{n[list_number]}')
            if await check_user_answer(user_id, message):
                await message.answer(message.from_user.id, f'{n[list_number+1]}')
            else:
                break
    except (Exception, ) as ex:
        print('ERROR', ex)


# Достаю все переводы из бд
async def get_translation(user_id):
    connection.autocommit = True
    try:
        cursor.execute(
            f"""
            SELECT translation FROM user_{user_id};
            """
        )
        global translations
        translations = cursor.fetchone()[0]

    except (Exception, ) as ex:
        print('ERROR', ex)


# Функция для проверки ответа пользователя
async def check_user_answer(user_id, message: aiogram.types.Message):
    await get_translation(user_id)
    for _ in translations:
        await bot.message_answer(message.from_user.id, 'Введіть переклад!')
        if message.text == translations:
            await message.reply('Вірно!')
        else:
            await message.reply('Помилка!')


def sql_shutdown():
    if connection:
        cursor.close()
        connection.close()
        print("[SUCCESS] PostgreSQL connection closed")
