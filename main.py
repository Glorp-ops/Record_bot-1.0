import asyncio
import logging
import os
from dotenv import load_dotenv
from Handler import handler
from aiogram import Bot, Dispatcher
from Middleware.db import DbSessionMiddleware
from DataBase.model import async_main

load_dotenv()
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()


# Run the bot
async def main() -> None:

    await async_main()

    logging.basicConfig(level=logging.INFO)
    dp.include_router(router=handler.rt)
    bot = Bot(token= TOKEN)

    dp.update.middleware(DbSessionMiddleware())
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
