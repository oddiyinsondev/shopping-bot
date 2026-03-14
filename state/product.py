from aiogram.fsm.state import State, StatesGroup


class ProductState(StatesGroup):
    category = State()
    name = State()
    price = State()
    image = State()
    check = State()