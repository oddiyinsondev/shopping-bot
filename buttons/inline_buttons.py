from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from db.main import ReadCategory, ReadProduct


def Menyu(category):
    buttons = InlineKeyboardBuilder()
    for i in category:
        buttons.add(InlineKeyboardButton(text=f"{i[-1]}", callback_data=f"{i[-1]}"))
    buttons.add(InlineKeyboardButton(text="Bog'lanish 👨‍💻", callback_data="bog"))
    buttons.add(InlineKeyboardButton(text="Karzinka 🛒", callback_data="cart"))
    buttons.add(InlineKeyboardButton(text="online shopping", web_app=WebAppInfo(url="https://gavharestaurant.uz/?category_id=31&locale=uz&subcategory_id=60")))
    buttons.adjust(2)
    return buttons.as_markup()    
        

