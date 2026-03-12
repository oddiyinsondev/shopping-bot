from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from db.main import ReadUser, AddUsers, ReadCategory
from buttons.inline_buttons import Menyu

start_router = Router()



@start_router.message(CommandStart())
async def StartBot(message: Message):
    user_id = message.from_user.id
    fullname = message.from_user.full_name
    if ReadUser(user_id=user_id) == None:
        AddUsers(user_id=user_id, fullname=fullname)
        await message.answer("Assalomu alaykum botga Xush kelibsiz", reply_markup=Menyu(category=ReadCategory()))
    else:
        await message.answer("Asosiy sahifadasiz", reply_markup=Menyu(category=ReadCategory()))
    