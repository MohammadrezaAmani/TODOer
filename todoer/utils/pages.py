from pyrogram.types import (
    ReplyKeyboardMarkup as RKM,
    InlineKeyboardMarkup as IKM,
    InlineKeyboardButton as IKB,
    InlineQueryResultArticle as IQRA,
    InputTextMessageContent as ITMC,
)
import enum
from todoer.utils.messages import Messages


class Pages(enum.Enum):
    HOME = RKM(
        [
            [Messages.TASK.value, Messages.REMINDER.value],
            [
                Messages.PLOT.value,
                Messages.MY_PROFILE.value,
            ],
        ],
        resize_keyboard=True,
    )
