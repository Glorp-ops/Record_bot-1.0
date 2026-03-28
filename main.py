import asyncio
import logging
import os
from dotenv import load_dotenv
from DataBase.model import async_main
from DataBase.requests import add_lesson
from Handler import handler
from aiogram import Bot, Dispatcher

load_dotenv()
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()

# Run the bot
async def main() -> None:
    await async_main()

    logging.basicConfig(level=logging.INFO)
    dp.include_router(router=handler.rt)
    bot = Bot(token= TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
