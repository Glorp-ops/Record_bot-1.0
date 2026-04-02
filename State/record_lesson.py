from aiogram.fsm.state import StatesGroup, State


class RecordLesson(StatesGroup):
    choose_lesson = State()
    choose_data = State()
    choose_time = State()
    add_record = State()