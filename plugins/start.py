
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
	wish = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ."
elif 12 <= currentTime.hour < 12:
	wish = 'Gᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ.'
else:
	wish = 'Gᴏᴏᴅ ᴇᴠᴇɴɪɴɢ.'

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
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
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
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
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
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__You are not subscribed my channel__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Join Our Update Channel" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("Use About cmd first /about")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 300
       else:
           LIMIT = 10
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"`Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}`",reply_to_message_id = message.id)
       else:
       		#await client.forward_messages(log_channel, message.from_user.id, message.id)
       		#await client.send_message(log_channel,f"User Id :- {user_id}")       		
           		
       		media = await client.get_messages(message.chat.id,message.id)
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
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)
       			if user_type == "NORMAL":
       				usertype(message.from_user.id,"Free")
			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I can't upload files that are larger than {humanbytes(limit)}. File size detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want to Rename Large File Upgrade Your Plan ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "premium") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳", callback_data = "premium") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__𝙒𝙝𝙖𝙩 𝘿𝙤 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝘿𝙤 𝙒𝙞𝙩𝙝 𝙏𝙝𝙞𝙨 𝙁𝙞𝙡𝙚𝙨 ?_\n\n𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞 :- {filename}\n𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 :- {humanize.naturalsize(file.file_size)}\n𝐃𝐜 𝐈𝐝 :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("🔐 ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            backpre(message.from_user.id)
	
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            backpre(message.from_user.id)       		            
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__𝙒𝙝𝙖𝙩 𝘿𝙤 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝘿𝙤 𝙒𝙞𝙩𝙝 𝙏𝙝𝙞𝙨 𝙁𝙞𝙡𝙚𝙨 ?__\n\n𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞 :- {filename}\n𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 :- {filesize}\n𝐃𝐜 𝐈𝐝 :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("🔐 ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
