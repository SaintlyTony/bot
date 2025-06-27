from aiogram.utils.keyboard import InlineKeyboardBuilder


def workout_menu(workout_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Выполнено", callback_data=f"done:{workout_id}")
    builder.button(text="Сохранить", callback_data=f"save:{workout_id}")
    builder.button(text="Следующая", callback_data="next")
    builder.adjust(3)
    return builder.as_markup()
