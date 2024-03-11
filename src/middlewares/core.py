from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from sqlalchemy.orm import Session

from src.domain import engine
from src.domain.repository.implement import UserRepository, ContactRepository

from src.content import KeyboardManager
from src.services import Services, RepositoryService, ContentService


class CoreMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ):
        session = Session(engine)

        data["services"] = Services(
            RepositoryService(
                user_repository=UserRepository(session),
                contact_repository=ContactRepository(session)
            ),
            ContentService(
                keyboards=KeyboardManager()
            )
        )

        await handler(event, data)

        storage_record = list(data["fsm_storage"].storage.values())[0]
        data["services"].repository.user_repository.save_state(
            event.message.from_user.id, storage_record.state, storage_record.data
        )
