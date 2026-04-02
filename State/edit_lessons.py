from aiogram.fsm.state import StatesGroup,State

class EditLessons(StatesGroup):

    add_lesson = State()
    upd_lesson = State()
    send_upd_message = State()
    new_lesson = State()
    del_lesson = State()