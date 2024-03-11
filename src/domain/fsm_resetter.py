import json

from typing import TYPE_CHECKING, List, Dict, Any
from dataclasses import dataclass

if TYPE_CHECKING:
    from src.domain.entities import User

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.base import StorageKey

from .repository.abstract import IUserRepository
from src import states


@dataclass
class FSMData:
    context: FSMContext
    state: str
    state_data: Dict[str, Any]


class FSMResetter:
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository: IUserRepository = user_repository

    def __get_user_states(
            self,
            bot: Bot,
            storage: BaseStorage
    ):
        users: List[User] = self.__user_repository.get_all()

        if not users:
            return

        users_fsm = []

        for user in users:
            user_id = user.user_id
            chat_id = user.chat_id
            state = user.state
            state_data = json.loads(user.state_data.replace("\'", "\""))

            storage_key = StorageKey(bot.id, chat_id, user_id)
            fsm_context = FSMContext(storage, storage_key)

            users_fsm.append(FSMData(fsm_context, state, state_data))

        return users_fsm

    async def reset_users_states(
            self,
            bot: Bot,
            storage: BaseStorage
    ):
        users_fsm: List[FSMData] = self.__get_user_states(bot, storage)

        if not users_fsm:
            return

        for fsm in users_fsm:
            state_name = fsm.state.split(":")
            state_class = getattr(states, state_name[0])
            state_object = getattr(state_class, state_name[1])

            await fsm.context.set_state(state_object)
            await fsm.context.update_data(**fsm.state_data)
