from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.services import Services

from src.domain.entities import User

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message, state: FSMContext, services: Services):
    await state.clear()
    await message.answer("Anus")

    services.repository.user_repository.add(
        User(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
            name=message.from_user.first_name,
            status="User"
        )
    )
