from pyrogram import Client
from .config import API_ID, API_HASH, BOT_TOKEN

if __name__ == "__main__":

    plugins = dict(
        root="todoer.plugins",
        include=[
            "start.start",
        ],
    )
    Client(
        "Todoer",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=plugins,
        proxy=dict(scheme="socks5", hostname="127.0.0.1", port=1089),
    ).run()
