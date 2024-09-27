from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
import sys
import re
import os

bot = Client("bot",
             bot_token=os.environ.get("BOT_TOKEN"),
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"))

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hello Bruh! I am TXT file Dowloader Bot** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n 馃煝 **Press /vicky then download video by txt**")

@bot.on_message(filters.command("Stop"))
async def restart_handler(_, m):
    await m.reply_text("馃殾**STOPPED**馃殾", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["hackheist"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('**Send TXT file for download**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    path = f"./downloads/{m.chat.id}"
    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send /d for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '/d':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter Your Name or send `op` for use default**")
    input15: Message = await bot.listen(editable.chat.id)
    raw_text15 = input15.text
    await input15.delete(True)
    highlighter = f" "
    if raw_text15 == 'op':
        OP = highlighter 
    else:
        OP = raw_text15

    await editable.edit("**Enter Your website url or send `loda` for use default**")
    input13: Message = await bot.listen(editable.chat.id)
    raw_text13 = input13.text
    await input13.delete(True)
    highlighter = f" "
    if raw_text13 == 'website':
        website = highlighter 
    else:
        website = raw_text15

    await editable.edit("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080"
        else: 
            res = "UN"
    except Exception:
        res = "UN"

    await editable.edit("**Enter Your Name or send `de` for use default**")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #Bot Created by @NtrRazYt
    input3: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #Bot Created by @NtrRazYt
    raw_text3 = input3.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #Bot Created by @NtrRazYt
    await input3.delete(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #Bot Created by @NtrRazYt
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'de':
        MR = highlighter 
    else:
        MR = raw_text3
  
    await editable.edit("Now send the **Thumb url**\nEg : `https://graph.org/file/45f562dc05b2874c7277e.jpg`\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(raw_text) if len(links) > 1 else 1

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={...}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={...}).json()['url']

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace(...).strip()
            name = f'{OP} {MR} {name1[:60]}'

            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                caption = f'{name1} {MR}.pdf\n\n **鉁� Batch 鉃� **{b_name}\n\n**<b>馃檹{MR} | <a href="https://yashyasag.github.io/hiddens_officials">饾悗饾悢饾悜 饾悥饾悇饾悂饾悞饾悎饾悡饾悇馃弲</a></b>'
                
                if "drive" in url:
                    ka = await helper.download(url, name)
                    copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=caption, thumb=thumb)
                    os.remove(ka)

                elif ".pdf" in url:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    os.system(f"{cmd} -R 25 --fragment-retries 25")
                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=caption, thumb=thumb)
                    os.remove(f'{name}.pdf')

                else:
                    prog = await m.reply_text(f"Downloading {name}")
                    filename = await helper.download_video(url, cmd, name)
                    await prog.delete()
                    await helper.send_vid(bot, m, caption, filename, thumb, name, prog)

            except Exception as e:
                await m.reply_text(f"**Failed to Download/Extract 馃槴**\n\n**Name** - {name1}\n**Link** - {url}\n\nSorry DADDY 馃檹")
                continue

    except Exception as e:
        await m.reply_text(e)
    
    await m.reply_text("**Done鉁�**")

bot.run()
