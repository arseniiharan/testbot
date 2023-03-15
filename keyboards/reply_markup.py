from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Додати слова')
        ],
        [
            KeyboardButton('Навчання')
        ],
        [
            KeyboardButton('Скинути мої слова')
        ],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
