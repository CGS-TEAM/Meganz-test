import os
from sample_config import Config
from translation import Translation
from pyrogram import Client as app
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Call backs @CGSUPDATES 

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "jsjsjp":
        await message.message.edit_text(
            text=exe.HELP_USER.format(message.from_user.mention),
            reply_markup=Translation.btns,
            disable_web_page_preview=True,
        )
    elif message.data == "helpback":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention),
            reply_markup=Translation.btn,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_USER.format(message.from_user.mention),
            reply_markup=Translation.btns,
            disable_web_page_preview=True
        )
    elif message.data == "refreshme":
        if Config.UPDATES_CHANNEL:
            invite_link = await client.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
            try:
                user = await client.get_chat_member(int(Config.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await message.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/CGSSUPPORT).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.message.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await message.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/CGSSUPPORT).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await message.message.edit(
            text=Translation.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.btn,
        )
    else:
        await message.message.delete()
