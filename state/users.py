from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    categorys = State()
    name = State()