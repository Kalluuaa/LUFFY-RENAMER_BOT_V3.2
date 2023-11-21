import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- <a href="https://telegram.dog/eliterenamebot">𝟺ɢʙ Rᴇɴᴀᴍᴇʀ Bᴏᴛ</a>\nCreater :- <a href="https://god_luffy_ati">𓊈𒆜. ɪᴛ'ꜱ ʟᴜғғʏ 𒆜𓊉</a>\nLanguage :-Python3\nLibrary :- Pyrogram 2.0\nServer :- Unknown\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
