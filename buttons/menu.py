from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def MenyuBot(products):
    buttons = InlineKeyboardBuilder()
    for product in products:
        buttons.add(InlineKeyboardButton(text=f"{product[2]}", callback_data=f"{product[2]}"))
    buttons.add(InlineKeyboardButton(text="ortga", callback_data='ortga'))
    buttons.adjust(2)
    return buttons.as_markup()
    
def Soni():
    buttons = InlineKeyboardBuilder()
    for i in range(1, 10):
        buttons.add(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
    buttons.add(InlineKeyboardButton(text="ortga", callback_data="back"))
    buttons.adjust(3)
    return buttons.as_markup()