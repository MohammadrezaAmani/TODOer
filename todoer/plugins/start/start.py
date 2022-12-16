import pyrogram
from pyrogram import Client, filters
from todoer.utils.steps import UserSteps
from todoer.utils.uxhandler import UXTree

@Client.on_message(filters.command("start"))
def start(client, message):
    step = UserSteps.START.value
    user = UXTree.nodes[step]
    message.reply_text(user.description, reply_markup=user.keyboard)