import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from sqlalchemy.orm import Session

from domain.repository.implement import UserRepository
from domain import engine, FSMResetter

from handlers import start, menu
from middlewares import CoreMiddleware


async def main():
    dispatcher = Dispatcher(storage=MemoryStorage())
    bot = Bot(str(os.getenv("BOT_TOKEN")), parse_mode=ParseMode.HTML)

    dispatcher.include_routers(
        start.router,
        menu.router
    )

    dispatcher.update.middleware.register(CoreMiddleware())

    fsm_resetter = FSMResetter(UserRepository(Session(engine)))
    await fsm_resetter.reset_users_states(bot=bot, storage=dispatcher.fsm.storage)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
