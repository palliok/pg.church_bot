from aiogram import types


async def answer_message(message: types.Message):
    """Хендлер на неопределенные сообщения."""

    await message.answer(
        "<b>Что-то пошло не так...</b>"
        "\n\n/menu чтобы вернуть в главное меню.",
        disable_notification=True,
    )
