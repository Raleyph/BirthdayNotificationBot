from aiogram.fsm.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    enter_user_name = State()
    enter_user_birthday = State()
    confirm = State()


class MenuStates(StatesGroup):
    main_menu = State()
    manage_contacts = State()


class AddContactStates(StatesGroup):
    change_input_type = State()
    enter_contact_name = State()
    enter_contact_birthday = State()


class EditContactStates(StatesGroup):
    edit_contact_name = State()
    edit_contact_birthday = State()
