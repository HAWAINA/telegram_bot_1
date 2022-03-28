import asyncio

from aiogram import executor, types, bot
from bot_instance import dp
from handers import callback_harry_potter, callback_home_work, \
    callback_problem, callback_quiz, callback_quizCars, client, \
    extra, fsmadmin
from database import bot_db
from handers.notification import scheduler


async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(scheduler())
    print("Bot is online")


fsmadmin.register_handler_fsmadmin(dp)
client.register_handlers_client(dp)

callback_quiz.register_handler_callback_quiz(dp)
callback_problem.register_handlers_callback_problem(dp)
callback_home_work.register_handlers_callback_homeWork(dp)
callback_quizCars.register_handlers_callback_homeWork(dp)
callback_harry_potter.register_handlers_callback_homeWork(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
