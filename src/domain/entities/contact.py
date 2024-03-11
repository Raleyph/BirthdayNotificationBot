from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column

from src.domain.repository import Base


class Contact(Base):
    __tablename__ = "contacts"

    user_id = mapped_column(Integer, nullable=False, unique=True)
    name = mapped_column(String, nullable=False)
    birthday = mapped_column(DateTime, nullable=False)
