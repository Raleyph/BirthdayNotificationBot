from typing import List, Type
from datetime import datetime

from src.domain.entities import Contact
from src.domain.repository.abstract import IContactRepository
from src.domain.repository import commit

from sqlalchemy.orm import Session


class ContactRepository(IContactRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_all(self) -> List[Type[Contact]]:
        return self.__session.query(Contact).all()

    def get_all_for_user(self, user_id: int) -> List[Type[Contact]]:
        return self.__session.query(Contact).filter(Contact.user_id == user_id).all()

    def get(self, contact_id: int) -> Type[Contact]:
        return self.__session.query(Contact).filter(Contact.id == contact_id).one()

    def add(self, contact: Contact) -> bool:
        self.__session.add(contact)
        return commit(self.__session)

    def update(self, contact_id: int, name: str, birthday: datetime) -> bool:
        contact = self.get(contact_id)
        contact.name = name
        contact.birthday = birthday

        self.__session.add(contact)
        return commit(self.__session)

    def delete(self, contact_id: int) -> bool:
        self.__session.delete(self.get(contact_id))
        return commit(self.__session)
