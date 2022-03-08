import os
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

uchannel = "CGSUpdates"

async def ForceSub(bot: Client, event: Message):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(uchannel) if uchannel.startswith("-100") else uchannel))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Unable to do Force Subscribe to {uchannel}\n\nError: {err}\n\nContact Support Group: https://t.me/CGSsupport")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(uchannel) if uchannel.startswith("-100") else uchannel), user_id=event.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text="Sorry Dear, You are Banned to use me ☹️\nFeel free to say in our [Support Group](https://t.me/CGSsupport).",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.chat.id,
            text=""" 
            ** {} NOT JOINED UPDATE CHANNEL **☹️

🪴[Join update channel](https://t.me/CGSUPDATES) to click button below or press /start ☘ Then try again.🍃


**@CGSUPDATES**🌺
            """.format(event.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                    ],
                    [   
                        InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                    ],
                ]
            ),
            disable_web_page_preview=True,
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Support Group: https://t.me/CGSsupport")
        return 200
    
