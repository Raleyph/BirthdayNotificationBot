from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import mapped_column

from src.domain.repository import Base


class User(Base):
    __tablename__ = "users"

    user_id = mapped_column(Integer, nullable=False, unique=True)
    chat_id = mapped_column(Integer, nullable=False, unique=True)
    name = mapped_column(String(32), unique=True)
    status = mapped_column(String, nullable=False)
    state = mapped_column(String)
    state_data = mapped_column(JSON)
