

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>🌷 𝗪ᴇʟᴄᴏᴍᴇ 𝗧ᴏ 𝗠ʏ 𝗕ᴏᴛ 𝗖ʀᴇᴀᴛᴇᴅ 𝗕ʏ 👉 @ITz_Tulip_XD</b> \n<b>Do /help 𝗙ᴏʀ 𝗠ᴏʀᴇ</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>🌷 sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴘʜᴏᴛᴏ/ᴠɪᴅᴇᴏ ɪ ᴡɪʟʟ ᴄᴏɴᴠᴇʀ ɪᴛ ɪɴᴛᴏ Telegra.ph.</b> \n<b>𝗖ʀᴇᴀᴛᴇᴅ 𝗕ʏ 👉 @ITz_Tulip_XD</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>ᴜᴘʟᴏᴀᴅɪɴɢ...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"🥺 𝗢ᴏᴘs!! 𝗦ᴏᴍᴇᴛʜɪɴɢ 𝗪ᴇɴᴛ 𝗪ʀᴏɴɢ\n{error} 𝗖ᴏɴᴛᴀᴄᴛ 👉 @ITz_Tulip_XD")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>ᴜᴘʟᴏᴀᴅɪɴɢ...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"🥺 𝗢ᴏᴘs!! 𝗦ᴏᴍᴇᴛʜɪɴɢ 𝗪ᴇɴᴛ 𝗪ʀᴏɴɢ\n{error} 𝗖ᴏɴᴛᴀᴄᴛ 👉 @ITz_Tulip_XD")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

