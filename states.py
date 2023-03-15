from aiogram.dispatcher.filters.state import State, StatesGroup


class OutputStates(StatesGroup):
    study_start = State()
    words_written = State()
