from aiogram import types
from bot import keyboards

async def toggle_timetable(message: types.Message):
    """Handler for toggle timetable."""

    user_id = message.from_user.id
    # is_liked = await db.is_liked(callback_data["idc"], user_id)

    # await db.toggle_like(not is_liked, callback_data["idc"], user_id)
    # await query.message.edit_reply_markup(
    #     keyboards.random_buttons(callback_data["idc"], is_like=not is_liked)
    # )
    # keyboard = keyboards.timetable_buttons()
    await message.answer('Расписание ...', reply_markup=keyboards.timetable_buttons())
    # await query.message.edit_reply_markup()

async def toggle_timetable_worship(message: types.Message):
    """Handler for toggle timetable."""

    text = '''30 апреля - 7 мая 2023

        Утренее богослужение: 30 апреля
        11:00-13:00

        Семинар
        14:00-16:00

        Вечернее богослужение
        17:00-19:00

        Молодежное общение
        19:00-21:00

        '''

    user_id = message.from_user.id
    # is_liked = await db.is_liked(callback_data["idc"], user_id)

    # await db.toggle_like(not is_liked, callback_data["idc"], user_id)
    # await query.message.edit_reply_markup(
    #     keyboards.random_buttons(callback_data["idc"], is_like=not is_liked)
    # )
    # keyboard = keyboards.timetable_buttons()
    await message.answer(text, reply_markup=keyboards.timetable_worship_buttons_moderator())
    # await query.message.edit_reply_markup()