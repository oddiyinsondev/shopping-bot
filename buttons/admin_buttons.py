from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Reklama ", callback_data='reklama')],
        [InlineKeyboardButton(text="Category", callback_data='category'), InlineKeyboardButton(text="Product", callback_data="product")]
    ]
)

