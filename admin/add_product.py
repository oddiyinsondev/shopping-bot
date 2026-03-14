from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from config.config import admins
from state.product import ProductState
from aiogram.fsm.context import FSMContext
from db.main import AddProduct, ReadCategory, ReadCategorys
from buttons.admin_buttons import CategoryButtons, tasdiq, menyu

addrouter = Router()


@addrouter.callback_query(F.data == "product", F.from_user.id.in_(admins))
async def ProductBot(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Product categoryasini tanlang", reply_markup=CategoryButtons(categors=ReadCategory()))
    await state.set_state(ProductState.category)

@addrouter.callback_query(ProductState.category, F.from_user.id.in_(admins))
async def Productname(call: CallbackQuery, state:FSMContext):
    xabar = call.data
    for i in ReadCategorys():
        if xabar == i[1]:
            id = i[0]
            await state.update_data(id=id, cate=xabar)
            await call.message.answer(text="maxsulotni nomini yuboring")
            await state.set_state(ProductState.name)
            break
    else:
        await call.answer("buttonlardan tanlang", show_alert=True)
        await state.set_state(ProductState.category)
        
@addrouter.message(ProductState.name, F.from_user.id.in_(admins))
async def Productcate(message:Message, state:FSMContext):
    xabar = message.text
    await state.update_data(nomi = xabar)
    await message.answer("narxini yuboring ... ")
    await state.set_state(ProductState.price)
    
    
@addrouter.message(ProductState.price, F.from_user.id.in_(admins))
async def Productnarx(message:Message, state:FSMContext):
    xabar = message.text
    await state.update_data(price = xabar)
    await message.answer("rasm yuboring ... ")
    await state.set_state(ProductState.image)
    
@addrouter.message(ProductState.image, F.from_user.id.in_(admins))
async def Productimage(message:Message, state:FSMContext):
    xabar = message.photo[-1].file_id
    await state.update_data(image = xabar)
    data = await state.get_data()
    id = data.get('id')
    category = data.get('cate')
    name = data.get('nomi')
    pul = data.get('price')
    await message.answer_photo(photo=xabar, caption=f"Categoryasi: {category}\nNomi: {name}\nPuli: {pul}", reply_markup=tasdiq)
    await state.set_state(ProductState.check)
    
@addrouter.message(ProductState.check, F.from_user.id.in_(admins))
async def Productimage(message:Message, state:FSMContext):
    xabar = message.text
    data = await state.get_data()
    id = data.get('id')
    category = data.get('cate')
    name = data.get('nomi')
    pul = data.get('price')
    image = data.get('image')
    if xabar == "Tasdiqlash ✅":
        AddProduct(name=name, category_id=int(id), price=int(pul), image=f"{image}")
        await message.answer("tasdiqlandi")
        await state.clear()
    else:
         await message.answer("Productni qaytadan kiriting ...", reply_markup=menyu)
         await state.clear()