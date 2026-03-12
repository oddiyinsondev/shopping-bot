from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from db.main import ReadUser, AddUsers, ReadCategory,AdsUsers
from buttons.admin_buttons import menyu
from config.config import admins
from aiogram.fsm.context import FSMContext
from state.reklama import Reklama


admin_router = Router()



@admin_router.message(CommandStart(), F.from_user.id.in_(admins))
async def StartBot(message: Message):
    await message.answer("Assalomu alaykum sizni kutyabmiz", reply_markup=menyu)


@admin_router.callback_query(F.data=='reklama', F.from_user.id.in_(admins))
async def ReklamaBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Reklamangizni yuboring ...")
    await state.set_state(Reklama.reklama)
    

@admin_router.message(Reklama.reklama)
async def ReklamaYuborish(message: Message, state:FSMContext):
    users = AdsUsers()
    for id in users:
        await message.copy_to(chat_id=id[0])
    await message.answer("reklama yuborildi")
    await state.clear()