from typing import List, Dict, Type, Any

from src.domain.entities import User
from src.domain.repository.abstract import IUserRepository
from src.domain.repository import commit

from sqlalchemy.orm import Session


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_all(self) -> List[Type[User]]:
        return self.__session.query(User).all()

    def get(self, user_id: int) -> Type[User]:
        return self.__session.query(User).filter(User.user_id == user_id).one()

    def add(self, user: User) -> bool:
        self.__session.add(user)
        return commit(self.__session)

    def save_state(self, user_id: int, state: str, state_data: Dict[str, Any]) -> bool:
        user: Type[User] = self.get(user_id)
        user.state = state
        user.state_data = state_data

        self.__session.add(user)
        return commit(self.__session)
