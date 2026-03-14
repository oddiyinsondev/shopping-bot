from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Reklama ", callback_data='reklama')],
        [InlineKeyboardButton(text="Category", callback_data='category'), InlineKeyboardButton(text="Product", callback_data="product")]
    ]
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tasdiqlash ✅"), KeyboardButton(text="Bekor qilish 🚫")]
    ], resize_keyboard=True
)


def CategoryButtons(categors):
    buttons = InlineKeyboardBuilder()
    for cat in categors:
        buttons.add(InlineKeyboardButton(text=f"{cat[0]}", callback_data=f"{cat[0]}"))
    buttons.add(InlineKeyboardButton(text="ortga", callback_data="ortga"))
    buttons.adjust(1)
    return buttons.as_markup()