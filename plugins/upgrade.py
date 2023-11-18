"""lokaman"""
import random
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from Script import script

elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ', url='https://t.me/elitecraft_Studios'),
            InlineKeyboardButton('🌿 sᴜᴘᴘᴏʀᴛ​', url='https://t.me/elitecraft_support')
            ],[      
            InlineKeyboardButton('💠 ʜᴇʟᴘ 💠', callback_data='help'),
            InlineKeyboardButton('✦ ᴀʙᴏᴜᴛ ✦', callback_data='about')
            ],[
            InlineKeyboardButton('Bᴜʏ Pʀᴇᴍɪᴜᴍ', callback_data='upgrade')
        ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('ᴛʜᴜᴍʙɴᴀɪʟ', callback_data='thumb'),
            InlineKeyboardButton('ᴄᴀᴘᴛɪᴏɴ', callback_data='caption')
        ], [
            InlineKeyboardButton('🛰 ʀᴇɴᴅᴇʀɪɴɢ ɪɴꜰᴏ ☁️', callback_data='rendering_info')
        ], [
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('sᴏᴜʀᴄᴇ', callback_data='source')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd `9480251952@paytm`
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("⇍ ʙᴀᴄᴋ ⇏",callback_data = "start")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd `9480251952@paytm`
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
