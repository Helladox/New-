import os
from config import CHANNEL_ID, SUDO_USERS 
from Extractor.core import script
from Extractor import app
from pyrogram.errors import UserNotParticipant
from pyrogram.types import *
from Extractor.core.mongo.plans_db import premium_users
from Extractor.core.mongo import db



async def chk_user(query, user_id):
    user = await premium_users()
    if user_id in user or user_id in SUDO_USERS:
        await query.answer("Premium User!!")
        return 0
    else:
        await query.answer("Sir, you don't have premium access!!", show_alert=True)
        return 1


async def gen_link(app,chat_id):
   link = await app.export_chat_invite_link(chat_id)
   return link


async def subscribe(app, message):
   update_channel = CHANNEL_ID
   url = await gen_link(app, update_channel)
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.from_user.id)
         if user.status == "kicked":
            await message.reply_text("Sorry Sir, You are Banned. Contact My Support Group @DevsOops")
            return 1
      except UserNotParticipant:
         await message.reply_photo(photo="https://telegra.ph/file/b7a933f423c153f866699.jpg",caption=script.FORCE_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 🤖", url=f"{url}")]]))
         return 1
      except Exception:
         await message.reply_text("Something Went Wrong. Contact My Support Group")
         return 1



async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""

        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1

        unit = ts[index:].lstrip()

        if value:
            value = int(value)

        return value, unit

    value, unit = extract_value_and_unit(time_string)

    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0




async def view_thumb(query):    
    data = await db.get_data(query.from_user.id)
    if data and data.get("thumb"):
       thumb = data.get("thumb")    
       await query.message.reply_photo(photo=thumb)
    else:
        await query.answer("ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ ᴛʜᴜᴍʙɴᴀɪʟ.", show_alert=True) 



async def remove_thumb(query):
    data = await db.get_data(query.from_user.id)  
    if data and data.get("thumb"):
        thumb = data.get("thumb")
        os.remove(thumb)
        await db.remove_thumbnail(query.from_user.id)
        await query.answer("ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.", show_alert=True)
    else:
        await query.answer("Empty !! Thumbnail", show_alert=True)
	

async def add_thumb(query):
    mkn = await app.ask(query.message.chat.id, text="Please send me your thumbnail photo.")
    if mkn.photo:
        file_name = str(query.from_user.id) + "thumb.jpg"
        photo_id = mkn.photo.file_id
        photo_path = await app.download_media(photo_id, file_name=file_name)
        await db.set_thumbnail(query.from_user.id, photo_path)
        await query.message.reply_text("✅️ Your thumbnail has been successfully saved.")
    else:
        await query.message.reply_text("❌️ Please send a valid photo for your thumbnail.")






