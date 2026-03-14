from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from config.config import admins
from state.category_state import CategoryState
from aiogram.fsm.context import FSMContext
from db.main import AddCategory
from buttons.admin_buttons import tasdiq

router_category = Router()

@router_category.callback_query(F.data == "category", F.from_user.id.in_(admins))
async def CategoryBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Category nomini kiriting....")
    await state.set_state(CategoryState.name)
    
@router_category.message(F.from_user.id.in_(admins), CategoryState.name)
async def CategorNameBot(message: Message, state:FSMContext):
    xabar = message.text
    await state.update_data(name=xabar)
    await message.answer("Tasdiqlaysizmi", reply_markup=tasdiq)
    await state.set_state(CategoryState.check)
    
    
@router_category.message(F.text, CategoryState.check)
async def TasdiqlashBot(message: Message, state: FSMContext):
    xabar = message.text
    if xabar == "Tasdiqlash ✅":
        data = await state.get_data()
        name = data.get('name')
        AddCategory(name)
        await message.answer("Tasdiqlandi")
        await state.clear()
    else:
        await message.answer("Category qaytadan kiriting ...")
        await state.set_state(CategoryState.name)