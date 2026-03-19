from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


delete_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="delete", callback_data='del', style='danger'), InlineKeyboardButton(text='ortga', callback_data='ortga', style='success')]
    ]
)