from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
    InlineKeyboardBuilder,
    InlineKeyboardMarkup
)

from aiogram.types import KeyboardButton, InlineKeyboardButton


class KeyboardManager:
    def __init__(self):
        self.__reset_builders()

    def __reset_builders(self):
        self.__r_keyboard = ReplyKeyboardBuilder()
        self.__i_keyboard = InlineKeyboardBuilder()

    def get_menu_keyboard(self) -> ReplyKeyboardMarkup:
        self.__reset_builders()
        self.__r_keyboard.row(KeyboardButton(text="🎂 Мои контакты"))
        return self.__r_keyboard.as_markup(resize_keyboard=True)

    def get_contact_keyboard(self, contact_id: int) -> InlineKeyboardMarkup:
        self.__reset_builders()
        self.__i_keyboard.row(InlineKeyboardButton(text="🖋 Редактировать", callback_data=f"edit:{contact_id}"))
        self.__i_keyboard.row(InlineKeyboardButton(text="❌ Удалить", callback_data=f"delete{contact_id}"))
        return self.__i_keyboard.as_markup()
