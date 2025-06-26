from aiogram import Router, types

router = Router()


@router.message(commands=["start"])
async def start_cmd(message: types.Message) -> None:
    await message.answer("Добро пожаловать в DareFitBot!")
