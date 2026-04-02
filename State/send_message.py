from aiogram.fsm.state import State,StatesGroup
class SendMessage(StatesGroup):
    message = State()