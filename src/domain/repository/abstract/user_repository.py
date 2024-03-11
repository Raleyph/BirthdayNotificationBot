from typing import List, Dict, Any
from abc import ABC, abstractmethod

from src.domain.entities import User


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def add(self, user: User) -> bool:
        pass

    @abstractmethod
    def save_state(self, user_id: int, state: str, state_data: Dict[str, Any]) -> bool:
        pass
