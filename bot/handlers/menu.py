from aiogram import types

from bot import keyboards, db

async def main_menu(query: types.CallbackQuery, callback_data: dict):
    """Handler for toggle timetable."""

    user_id = query.from_user.id
    # is_liked = await db.is_liked(callback_data["idc"], user_id)

    # await db.toggle_like(not is_liked, callback_data["idc"], user_id)
    # await query.message.edit_reply_markup(
    #     keyboards.random_buttons(callback_data["idc"], is_like=not is_liked)
    # )
    # keyboard = keyboards.timetable_buttons()
    await query.message.edit_text('Добро пожаловать')
    await query.message.edit_reply_markup(keyboards.main_buttons())

