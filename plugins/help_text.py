import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config as config
else:
    from config import Config

import time
import psutil
import shutil
import string
import asyncio
from asyncio import TimeoutError
from translation import Translation
from pyrogram import Client as app
from database.fsub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from database.blacklist import check_blacklist
from database.userchats import add_chat

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

KK_MSG = """
SOURCE - `https://github.com/XMYSTERlOUSX/mega-link-downloader-bot`
"""

@Client.on_message(filters.command("help"))
async def help_user(bot, update):
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    fuser = update.from_user.id
    if check_blacklist(fuser):
        await update.reply_text("Sorry! You are Banned!")
        return
    add_chat(fuser)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        reply_markup=Translation.btns,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.command("about"))
async def help_user(bot, update):
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    fuser = update.from_user.id
    if check_blacklist(fuser):
        await update.reply_text("Sorry! You are Banned!")
        return
    add_chat(fuser)
    await bot.send_message(
        chat_id=update.chat.id,
        text=KK_MSG,
        parse_mode="html",
        reply_markup=Translation.btns,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.command("start"))
async def start(bot, update):
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    fuser = update.from_user.id
    if check_blacklist(fuser):
        await update.reply_text("Sorry! You are Banned!")
        return
    add_chat(fuser)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=Translation.btn,
        disable_web_page_preview=True,
    )
@Client.on_message(filters.command("status") & filters.user(config.OWNER_ID))
async def show_status_count(_, client, Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await client.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`\n\n@CGSMEGANZBOT,"
    )
