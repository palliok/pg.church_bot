from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

main_cbd = CallbackData("main", "action")


def main_buttons() -> ReplyKeyboardMarkup:
    """Returns markup for /random audio buttons."""

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Расписание"), KeyboardButton("Объявления")
        ).row(
            KeyboardButton("Служения"), KeyboardButton("О церкви")
        ).row(
            KeyboardButton("Пожертвования")
        )


