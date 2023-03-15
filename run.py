from aiogram import executor

from main import dp
import handlers
from databases.postgresql_db import create_table

try:
    create_table()

except Exception as ex:
    print(ex)

handlers.register_output_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

