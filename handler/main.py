from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from db.main import ReadProduct, ReadCategorys, ReadProducts
from buttons.menu import MenyuBot
from state.users import UserState
from aiogram.fsm.context import FSMContext

router = Router()

            
@router.callback_query(F.data, UserState.categorys)
async def Menyubot(call: CallbackQuery):
    xabar = call.data
    malumot = ReadProducts(name=xabar)
    await call.message.answer_photo(photo=malumot[4], caption=f"Nomi: {malumot[2]}\nNarxi: {malumot[3]} so'm\n")


@router.callback_query(F.data)
async def Menyubot(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar == "bog":
        await call.message.answer("Admin nomer: +998 93 715 45 15")
    elif xabar == 'cart':
        await call.message.answer("Karzinka bo'limma ")
    else:
        for cat in ReadCategorys():
            if cat[1] == xabar: 
                await call.message.answer("menyudan birini tanlang", reply_markup=MenyuBot(products=ReadProduct(category_id=cat[0])))
                await state.set_state(UserState.categorys)
                break
        else:
            await call.answer("Bu yerda buttonlardan tanlang")