from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def MenyuBot(products):
    buttons = InlineKeyboardBuilder()
    for product in products:
        buttons.add(InlineKeyboardButton(text=f"{product[2]}", callback_data=f"{product[2]}"))
    buttons.add(InlineKeyboardButton(text="ortga", callback_data='ortga'))
    buttons.adjust(2)
    return buttons.as_markup()
    