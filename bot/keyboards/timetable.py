from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def timetable_buttons() -> ReplyKeyboardMarkup:

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Богослужения")
        ).row(
            KeyboardButton("Дежурства пасторов")
        ).row(
            KeyboardButton("Мероприятия")
        )

def timetable_worship_buttons_moderator() -> ReplyKeyboardMarkup:

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Редактировать"), KeyboardButton("Отправить уведомление")
        )

def timetable_worship_buttons_moderator_save() -> ReplyKeyboardMarkup:

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Сохранить")
        )

def timetable_worship_buttons_user_subscribe() -> ReplyKeyboardMarkup:

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Подписаться")
        )

def timetable_worship_buttons_user_unsubscribe() -> ReplyKeyboardMarkup:

    return ReplyKeyboardMarkup(
            resize_keyboard = True
        ).row(
            KeyboardButton("Отписаться")
        )
