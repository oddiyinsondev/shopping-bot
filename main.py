import asyncio
import logging
from aiogram import Dispatcher, Bot
from config.config import token, admins
from handler import start
from handler.main import router
from admin.main import admin_router
from admin import add_category, add_product


bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


async def main():
    for admin in admins:
        await bot.send_message(chat_id=admin, text="bot ishladi")
    # dp.include_routers(admin_router, add_category.router_category, add_product.addrouter)
    dp.include_routers(start.start_router, router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("tugadi")

