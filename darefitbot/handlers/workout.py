from aiogram import Router, types

from ..database import models
from ..utils import tools
from ..keyboards.workout_menu import workout_menu
from .ads import send_random_ad

router = Router()


@router.message(commands=["workout"])
async def workout_cmd(message: types.Message) -> None:
    user = models.get_user(message.from_user.id)
    workout = tools.select_workout(user.get("goals"), user.get("level"))
    if not workout:
        await message.answer("Тренировки не найдены.")
        return

    caption = f"{workout['title']}\n{workout.get('description', '')}"
    await message.answer_photo(
        types.FSInputFile(workout["image"]),
        caption=caption,
        reply_markup=workout_menu(workout["id"]),
    )
    print(f"[workout] Отправлена тренировка ID:{workout['id']}")

    if tools.should_send_ad(message.from_user.id):
        await send_random_ad(message)
