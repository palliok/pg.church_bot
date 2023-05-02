from sqlite3 import Error as SqliteError

from aiogram import Dispatcher
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher.filters import Text

from bot.utils.exceptions import QueueLimitReached
from bot.utils.logger import get_logger

from .commands import (
    command_start,
    command_about
)
from .common import answer_message
from .errors import (
    database_error,
    global_error_handler,
    message_not_modified_error,
    queue_limit_reached,
)
from .timetable import (
    toggle_timetable,
    toggle_timetable_worship
)

log = get_logger()

def register_handlers(dp: Dispatcher):

    log.info("Register Bot handlers...")
    dp.register_errors_handler(
        database_error,
        exception=SqliteError,
    )
    dp.register_errors_handler(
        message_not_modified_error,
        exception=MessageNotModified,
    )
    dp.register_errors_handler(
        queue_limit_reached,
        exception=QueueLimitReached,
    )
    dp.register_errors_handler(
        global_error_handler, exception=Exception
    )  # Should be last among errors handlers

    dp.register_message_handler(
        command_start,
        commands=["start", "menu"],
    )
    dp.register_message_handler(
        command_about,
        commands=["about"],
    )
    dp.register_message_handler(
        toggle_timetable,
        Text(equals="расписание", ignore_case=True)
    )
    dp.register_message_handler(
        toggle_timetable_worship,
        Text(equals="богослужения", ignore_case=True)
    )
    
    dp.register_message_handler(answer_message)
