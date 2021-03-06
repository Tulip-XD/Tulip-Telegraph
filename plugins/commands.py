

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>ð· ðªá´Êá´á´á´á´ ð§á´ ð Ê ðá´á´ ðÊá´á´á´á´á´ ðÊ ð @ITz_Tulip_XD</b> \n<b>Do /help ðá´Ê ð á´Êá´</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>ð· sá´É´á´ á´á´ á´É´Ê á´Êá´á´á´/á´ Éªá´á´á´ Éª á´¡ÉªÊÊ á´á´É´á´ á´Ê Éªá´ ÉªÉ´á´á´ Telegra.ph.</b> \n<b>ðÊá´á´á´á´á´ ðÊ ð @ITz_Tulip_XD</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>á´á´á´¡É´Êá´á´á´ÉªÉ´É¢...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>á´á´Êá´á´á´ÉªÉ´É¢...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"ð¥º ð¢á´á´s!! ð¦á´á´á´á´ÊÉªÉ´É¢ ðªá´É´á´ ðªÊá´É´É¢\n{error} ðá´É´á´á´á´á´ ð @ITz_Tulip_XD")
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
          text="<b>á´á´á´¡É´Êá´á´á´ÉªÉ´É¢...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>á´á´Êá´á´á´ÉªÉ´É¢...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"ð¥º ð¢á´á´s!! ð¦á´á´á´á´ÊÉªÉ´É¢ ðªá´É´á´ ðªÊá´É´É¢\n{error} ðá´É´á´á´á´á´ ð @ITz_Tulip_XD")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

