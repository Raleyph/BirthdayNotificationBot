from typing import List, Type
from abc import ABC, abstractmethod

from src.domain.entities import Contact


class IContactRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Type[Contact]]:
        pass

    @abstractmethod
    def get_all_for_user(self, user_id: int) -> List[Type[Contact]]:
        pass

    @abstractmethod
    def get(self, contact_id: int) -> Type[Contact]:
        pass

    @abstractmethod
    def add(self, contact: Contact) -> bool:
        pass

    @abstractmethod
    def delete(self, contact_id: int) -> bool:
        pass
