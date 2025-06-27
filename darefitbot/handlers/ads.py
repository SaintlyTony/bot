from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..utils import tools

router = Router()


async def send_random_ad(message: types.Message) -> None:
    ad = tools.select_ad()
    if not ad:
        return
    keyboard = None
    if ad.get("url"):
        builder = InlineKeyboardBuilder()
        builder.button(text=ad.get("button", "Подробнее"), url=ad["url"])
        keyboard = builder.as_markup()
    if ad.get("image"):
        await message.answer_photo(types.FSInputFile(ad["image"]), caption=ad.get("text", ""), reply_markup=keyboard)
    else:
        await message.answer(ad.get("text", ""), reply_markup=keyboard)
