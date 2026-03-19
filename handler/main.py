from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from buttons.delete import delete_buttons
from db.main import ReadProduct, ReadCategorys, ReadProducts, AddKarzinka, ReadKarzinka, ReadCategory, DeleteKarzinka
from buttons.menu import MenyuBot, Soni
from buttons.inline_buttons import Menyu
from state.users import ProductState
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data == "ortga")
async def OrtgaBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Asosiy sahifadasiz", reply_markup=Menyu(category=ReadCategory()))
    await state.clear()
    await call.message.delete()
            
@router.callback_query(F.data, ProductState.A)
async def Menyubot(call: CallbackQuery, state:FSMContext):
    xabar = call.data
    malumot = ReadProducts(name=xabar)
    data = await state.get_data()
    cat = data.get('cat')
    await call.message.answer_photo(photo=malumot[4], caption=f"Nomi: {malumot[2]}\nNarxi: {malumot[3]} so'm\n", reply_markup=Soni())
    await state.update_data({'name':malumot[2], "narx":malumot[3]})
    await call.message.delete()
    await state.set_state(ProductState.B)
    
    
@router.callback_query(F.data, ProductState.B)
async def KarzinkaBot(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    xabar = call.data
    if xabar.isalpha():
        await state.set_state(ProductState.A)
        data = await state.get_data()
        categry = data.get('cat')
        for cat in ReadCategorys():
            if cat[1] == categry: 
                await call.message.answer("menyudan birini tanlang", reply_markup=MenyuBot(products=ReadProduct(category_id=cat[0])))
                await state.update_data(cat=xabar)
                await call.message.delete()
    else:
        data = await state.get_data()
        cat = data.get('cat')
        name = data.get('name')
        narx = data.get('narx')
        AddKarzinka(user_id=user_id, name=name, price=narx, category=cat, soni=int(xabar))
        await call.message.answer("Asosiy sahifadasiz", reply_markup=Menyu(category=ReadCategory()))
        await call.message.delete()
        await state.clear()

@router.callback_query(F.data == 'del', ProductState.C)
async def DeleteBot(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    DeleteKarzinka(user_id=user_id)
    await call.message.answer("Asosiy sahifadasiz", reply_markup=Menyu(category=ReadCategory()))
    await state.clear()
    await call.message.delete()
        


@router.callback_query(F.data)
async def Menyubot(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    user_id = call.from_user.id
    if xabar == "bog":
        await call.message.answer("Admin nomer: +998 93 715 45 15")
        await call.message.delete()
    elif xabar == 'cart':
        malumot = ReadKarzinka(user_id)
        zakaz = f""
        narxi = 0
        for i in malumot:
            zakaz += f"Category: {i[4]}\nNomi: {i[2]}\nNarxi: {i[3]} so'm\nSoni: {i[5]} pors\n\n"
            narxi += i[3] * i[5]
        await call.message.answer(f"Karzinka bo'limi\n{zakaz}\nJami summa {narxi} so'm", reply_markup=delete_buttons)
        await state.set_state(ProductState.C)
        await call.message.delete()
    else:
        for cat in ReadCategorys():
            if cat[1] == xabar: 
                await call.message.answer("menyudan birini tanlang", reply_markup=MenyuBot(products=ReadProduct(category_id=cat[0])))
                await state.update_data(cat=xabar)
                await state.set_state(ProductState.A)
                await call.message.delete()
                break
        else:
            await call.answer("Bu yerda buttonlardan tanlang")