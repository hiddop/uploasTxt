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

links = []
                                                        
                                                        
                                                        
@bot.on_message(filters.text)
async def automatic_download(bot: Client, m: Message):
    try:
        cmd_text = m.text.split()

        # Validate message format and extract values
        if len(cmd_text) >= 2 and cmd_text[0].startswith("http"):
            url = cmd_text[0]
            nameop = re.search(r'-n\s+(\S+)', m.text)
            raw_text2 = re.search(r'-r\s+(\S+)', m.text)
            thumb = re.search(r'-t\s+(\S+)', m.text)
            


            # Set resolution format based on user input
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
                                                 
                                                         
                                                        
            if cmd_text[0].startswith("http"):
                V = cmd_text[0]
            
            # Apply transformations to the URL
            V = V.replace("file/d/", "uc?export=download&id=") \
                 .replace("www.youtube-nocookie.com/embed", "youtu.be") \
                 .replace("?modestbranding=1", "") \
                 .replace("/view?usp=sharing", "")

            url = "https://" + V                                                        
                                                        
            if "visionias" in url:                                                        
                async with ClientSession() as session:                                                        
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:                                                        
                        text = await resp.text()                                                        
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)                                                        
                                                        
            elif 'videos.classplusapp' in url:                                                        
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']                                                        
                                                        
            elif '/master.mpd' in url:                                                        
             id =  url.split("/")[-2]                                                        
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"                                                        
                                                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "@").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()                                                        
            name = f'{nameop} {name1[:60]}'                                                        
                                                        
            if "youtu" in url:                                                        
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"                                                        
            else:                                                        
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"                                                        
                                                        
            if "jw-prod" in url:                                                        
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'                                                        
            else:                                                        
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'                                                        
                                                        
            try:                                                          
                                                                        
                cc = f'**{name1}.mkv**\n\n**❃ 𝗕𝗮𝘁𝗰𝗵 » HACKHEIST**\n\n**♛ 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝔼𝔻 𝔹𝕐 ★**\n**━━━━━━━✦✗✦━━━━━━━**\n****'
                cc1 = f'**{name1}.pdf**\n\n**❃ 𝗕𝗮𝘁𝗰𝗵 » HACKHEIST**\n\n**♛ 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝔼𝔻 𝔹𝕐 ★**\n**━━━━━━━✦✗✦━━━━━━━**\n****'
                if "drive" in url:                                                        
                    try:                                                        
                        ka = await helper.download(url, name)                                                        
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)                                                        
                        count+=1                                                        
                        os.remove(ka)                                                        
                        time.sleep(1)                                                        
                    except FloodWait as e:                                                        
                        await m.reply_text(str(e))                                                        
                        time.sleep(e.x)                                                        
                                                                                
                                                                        
                elif ".pdf" in url:                                                        
                    try:                                                        
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'                                                        
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"                                                        
                        os.system(download_cmd)                                                        
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)                                                        
                        count += 1                                                        
                        os.remove(f'{name}.pdf')                                                        
                    except FloodWait as e:                                                        
                        await m.reply_text(str(e))                                                        
                        time.sleep(e.x)                                                        
                                                                                
                else:                                                        
                    Show = f"**⥥ 📥 ＤＯＷＮＬＯＤＩＮＧ 📥 :-**\n\n**📝Name »** `{name}\n❄𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**Url :-** `Kya karega URL dekhke ☠️☠️`\n\n **Bot made by HACKHEIST (Daddy)🧑🏻‍💻**"                                                        
                    prog = await m.reply_text(Show)                                                        
                    res_file = await helper.download_video(url, cmd, name)                                                        
                    filename = res_file                                                        
                    await prog.delete(True)                                                        
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)                                                        
                    count += 1                                                        
                    time.sleep(1)                                                        
                                                        
            except Exception as e:                                                        
                await m.reply_text(                                                        
                    f"**Failed to Download/Extract 😫**\n\n**Name** - {cc}\n**𝗟𝗜𝗡𝗞** - {url}\n\nSorry HACKHEIST 🙏**"                                                        
                )                                                        
                                                                        
                                                        
    except Exception as e:                                                        
        await m.reply_text(e)                                                        
    await m.reply_text("**Done✅**")                                                        
                                                        
                                                        
bot.run()                                                        
                                                        
