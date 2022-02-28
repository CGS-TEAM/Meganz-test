import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config as config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from database.blacklist import check_blacklist
from database.userchats import add_chat

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


# Leo Projects <https://t.me/leosupportx>
# @Naviya2 🇱🇰

import os
import time
import psutil
import shutil
import string
import asyncio
import config
from asyncio import TimeoutError
from LeoSongDownloaderBot.translation import Translation
from helper.database.access_db import db
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client as app
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram import idle, filters, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

CGSIMG = "https://telegra.ph/file/7a3ee0b1803ed6e6fbc87.jpg"

@app.on_message(filters.command("start"))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply_photo(
        CGSIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention),
        reply_markup=Translation.btn
    )
   

@app.on_message(filters.command("help"))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply_photo(
        CGSIMG,
        caption=Translation.HELP_USER.format(message.from_user.mention),
        reply_markup=Translation.btns
    )
    
@app.on_message(filters.private & filters.command("status") & filters.user(config.BOT_OWNER))
async def show_status_count(_, client: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await client.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`\n\n@leosongdownloaderbot 🇱🇰",
        parse_mode="Markdown",
        quote=True
    )
