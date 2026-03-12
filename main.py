import asyncio
import logging
from aiogram import Dispatcher, Bot
from config.config import token, admins
from handler import start
from admin.main import admin_router


bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


async def main():
    for admin in admins:
        await bot.send_message(chat_id=admin, text="bot ishladi")
    dp.include_router(admin_router)
    dp.include_routers(start.start_router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("tugadi")

