from aiogram import types

from bot import db, keyboards, version
from bot.utils.logger import get_logger

log = get_logger()


async def command_start(message: types.Message):
    """Handler for `/start` command."""

    log.info(
        "User join: %s <%s>", message.from_user.id, message.from_user.username
    )
    await db.add_user(message.from_user.id, message.from_user.username)

    await message.answer(
            "Добро пожаловать",
            reply_markup=keyboards.main_buttons()
        )


async def command_help(message: types.Message):
    """Handler for `/help` command."""

    await message.answer(
        "<b>Available commands:</b>"
        "\n\n/random to get and listen shared tunes."
        "\n/about additional info and author contacts."
        "\n\n<b>How it works:</b>"
        "\n\nThis Bot slowing down your audio at 33/45 vinyl rpm ratio. "
        "You can share your result slowed audio with other users by "
        "<code>share button</code> and promote by <code>like button</code>. "
        "You can also report any shared audio to have it removed "
        "from public access.",
        disable_notification=True,
    )


async def command_about(message: types.Message):
    """Handler for `/about` command."""

    users_count = await db.users_count()
    slowed_count = await db.slowed_count()
    random_count = await db.random_count()

    await message.answer(
        "This bot is written in Python with the aiogram and sox modules. "
        "It uses Redis and SoX services. Enjoy!"
        "\n\n<b>Copyrights notice</b>: "
        "All audio tracks belong to their respective owners "
        "and author of this bot does not claim any right over them. "
        "The uploaded files are stored on the Telegram servers and "
        "are downloaded by the user directly from there."
        f"\n\n<b>Users</b>: {users_count}"
        f"\n<b>Slowed tunes</b>: {slowed_count}"
        f"\n<b>Shared tunes</b>: {random_count}"
        "\n\n<b>Author</b>: "
        "<a href='https://t.me/paulsukharev'>@paulsukharev</a>"
        "\n<b>Source</b>: "
        "<a href='https://github.com/palliok'>Github</a>"
        f"\n<b>Version</b>: {version}",
        disable_notification=True,
        disable_web_page_preview=True,
    )
