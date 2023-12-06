from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
import os
import re, asyncio, os, sys
import os, asyncio
import pymongo
import random
import shutil, psutil, time
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.progress import get_size, get_time, humanbytes
from Script import script
from helper.database import  find_one,used_limit 
from helper.database import daily as daily_ 
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size,usertype,backpre
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL", "-1002066295284"))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]

DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["promo"]
total, used, free = shutil.disk_usage(".")
BOT_START_TIME = time.time()

def profind(id):
	return dbcol.find_one({"_id":id})


#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Gᴏᴏᴅ Mᴏʀɴɪɴɢ."
elif 12 <= currentTime.hour < 12:
	wish = 'Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ.'
else:
	wish = 'Gᴏᴏᴅ Eᴠᴇɴɪɴɢ.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	user_id = message.from_user.id
	letdata = profind(int(user_id))
	try:
	    procode = letdata["promo"]
	except:
	    pass	
	try:
	    id = message.text.split(' ')[1]
	except:
	    m=await message.reply_sticker("CAACAgQAAxkBAAJ2AAFlXKy5e11B5VhTg4YFfLSdZlqHbwACbg8AAuHqsVDaMQeY6CcRoh4E") 
	    await asyncio.sleep(1)
	    await m.delete()
	    await message.reply_photo(photo ="https://graph.org/file/43f5c07fe7c7021b5e44a.jpg",
		    caption =script.START_TXT.format(wish, message.from_user.mention), 
          reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Uᴘᴅᴀᴛᴇ" ,url="https://t.me/Max_Leech_Zone_Update"), InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/Noobseverywhere")], 
	[InlineKeyboardButton("• Hᴇʟᴘ •", callback_data="help"), InlineKeyboardButton("• Aʙᴏᴜᴛ •", callback_data="about") ],
	 [InlineKeyboardButton("💰 Uᴘɢʀᴀᴅᴇ Tᴏ Pʀᴇᴍɪᴜᴍ 💰", callback_data="premium") ]]))
	    return
	if id:
	        if id == procode:
	            await message.reply_text("You Can Use Now ")
	            uploadlimit(int(user_id),10737418240)
	            usertype(int(user_id),"NORMAL")

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=script.START_TXT.format(wish, query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/Max_Leech_Zone_Update'),
                InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/Noobseverywhere')
                ],[
                InlineKeyboardButton('• Hᴇʟᴘ •', callback_data='help'),
                InlineKeyboardButton('• Aʙᴏᴜᴛ •', callback_data='about')
            ],[
                InlineKeyboardButton('💰 Uᴘɢʀᴀᴅᴇ Tᴏ Pʀᴇᴍɪᴜᴍ 💰', callback_data='premium')
            ]])
	)
    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="thumb"),
		InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="caption")
                ],[
                InlineKeyboardButton("↻ ʀᴇɴᴅᴇʀɪɴɢ ɪɴғᴏ ↺", callback_data='rendering_info')
                ],[
                InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data = "source")
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
            ]])            
	)
    elif data == "premium":
        await query.message.edit_text(
            text=script.PREMIUM_TXT.format(query.from_user.mention, query.from_user.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("⇚ 𝐁𝐚𝐜𝐤", callback_data = "start"), 
            InlineKeyboardButton('𝐂𝐨𝐧𝐭𝐚𝐜𝐭 ↝', url='https://t.me/mr_kallua')
            ]])            
        )
    elif data == "free":
        await query.message.edit_text(
            text=script.FREE_PLAN,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "silver":
        await query.message.edit_text(
            text=script.SILVER_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url = "https://t.me/god_luffy_ati")
            ],[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "gold":
        await query.message.edit_text(
            text=script.GOLDEN_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url = "https://t.me/god_luffy_ati")
            ],[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "diamond":
        await query.message.edit_text(
            text=script.DIAMOND_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url = "https://t.me/god_luffy_ati")
            ],[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)
    elif data == "thumb":
        await query.message.edit_text(
            text=script.THUMB_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⇚ ʙᴀᴄᴋ", callback_data = "help")
            ]])            
	)
    elif data == "caption":
        await query.message.edit_text(
            text=script.CAPTION_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])            
	)
    elif data == "source":
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])            
	)
	    #---------------------------Bot rendring stats-----------------------#
    elif data == "rendering_info":
        await query.answer(text=script.STATS.format(get_time(time.time() - BOT_START_TIME), psutil.cpu_percent(), psutil.virtual_memory().percent, humanbytes(total), humanbytes(used), psutil.disk_usage('/').percent, humanbytes(free)), show_alert=True)
	    #-----------------------------bot stats-------------------------------#

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:	
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__𝗬𝗼𝘂 𝗔𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("⚜ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #rename_logs 🦋,\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n Uꜱᴇʀ-Pʟᴀɴ : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Rᴇꜱᴛʀɪᴄᴛ Uꜱᴇʀ ( PM ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Uꜱᴇ Aʙᴏᴜᴛ ᴄᴍᴅ Fɪʀꜱᴛ /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"Hello dear {message.from_user.first_name}  Wᴇ Aʀᴇ Cᴜʀʀᴇɴᴛʟʏ Wᴏʀᴋɪɴɢ Oɴ Tʜɪꜱ Iꜱꜱᴜᴇ \n\n Pʟᴇᴀꜱᴇ Tʀʏ Tᴏ Rᴇɴᴀᴍᴇ Fɪʟᴇꜱ Fʀᴏᴍ Yᴏᴜʀ Aɴᴏᴛʜᴇʀ Aᴄᴄᴏᴜɴᴛ.\n Bᴇᴄᴀᴜꜱᴇ Tʜɪꜱ BOT Cᴀɴ'ᴛ Rᴇɴᴀᴍᴇ Fɪʟᴇ Sᴇɴᴛ Bʏ Sᴏᴍᴇ Iᴅꜱ.\n\nIғ Yᴏᴜ Aʀᴇ Aɴ ADMIN Dᴏɴ'ᴛ Wᴏʀʀʏ ! Hᴇʀᴇ Wᴇ Hᴀᴠᴇ A Sᴏʟᴜᴛɪᴏɴ Fᴏʀ Yᴏᴜ Dᴇᴀʀ {message.from_user.first_name }.\n\n Pʟᴇᴀꜱᴇ Uꜱᴇ\n👉 `/addpremium ʏᴏᴜʀ_ᴏᴛʜᴇʀ_ᴜꜱᴇʀɪᴅ` 👈 Tᴏ Uꜱᴇ Pʀᴇᴍɪᴜᴍ Fᴇᴀᴜᴛʀᴇ\n\n",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("🦋 Contact Owner 🦋", url='https://telegram.me/mr_kallua')]                                                             
                                                                    ]))
        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 10
    else:
        LIMIT = 00
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sᴏʀʀʏ Dᴜᴅᴇ I Aᴍ Nᴏᴛ Oɴʟʏ Fᴏʀ YOU \nFʟᴏᴏᴅ Cᴏɴᴛʀᴏʟ Iꜱ Aᴄᴛɪᴠᴇ Aᴏ Pʟᴇᴀꜱᴇ Wᴀɪᴛ Fᴏʀ {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"**❗️ 𝟷𝟶𝟶% Oғ Dᴀɪʟʏ {humanbytes(limit)} Dᴀᴛᴀ Qᴜᴏᴛᴀ Exʜᴀᴜꜱᴛᴇᴅ**.\n\n 📁 Fɪʟᴇ Sɪᴢᴇ Dᴇᴛᴇᴄᴛᴇᴅ = {humanbytes(file.file_size)}\n ℹ️ Uꜱᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ = {humanbytes(used)}\n\n Yᴏᴜ Hᴀᴠᴇ Oɴʟʏ {humanbytes(remain)} Lᴇғᴛ Oɴ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ.\nIғ U Wᴀɴᴛ Tᴏ Rᴇɴᴀᴍᴇ Lᴀʀɢᴇ Fɪʟᴇ Yᴏᴜ Nᴇᴇᴅ Tᴏ Uᴘɢʀᴀᴅᴇ Yᴏᴜʀ Pʟᴀɴ 💡", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" Yᴏᴜ Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Mᴏʀᴇ Tʜᴇɴ {humanbytes(limit)} Uꜱᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪꜱ Fɪʟᴇ?__\n\n𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- <code>{filename}</code>\n𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲 :- {humanize.naturalsize(file.file_size)}\n𝗗𝗖 𝗜𝗗 :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Yᴏᴜʀ Pʟᴀɴ Exᴘɪʀᴇᴅ Oɴ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 𝟸GB 😔")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪꜱ Fɪʟᴇ?__\n\n𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- <code>{filename}</code>\n𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲:- {filesize}\n𝗗𝗖 𝗜𝗗 :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ", callback_data="cancel")]]))
