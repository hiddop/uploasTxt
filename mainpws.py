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
import tempfile
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import datetime
import aiohttp
                                                        
bot = Client("bot",                                                        
             bot_token=os.environ.get("BOT_TOKEN"),                                                        
             api_id=int(os.environ.get("API_ID")),                                                        
             api_hash=os.environ.get("API_HASH"))                                                        
                                                        
                                                        
@bot.on_message(filters.command("Stop"))                                                        
async def restart_handler(_, m):                                                        
    await m.reply_text("🚦**STOPPED**🚦", True)                                                        
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command('h2t'))
async def run_bot(bot: Client, m: Message):
    editable = await m.reply_text("Send Your HTML file\n")
    input: Message = await bot.listen(editable.chat.id)
    html_file = await input.download()
    await input.delete(True)
    await editable.delete()

    # Open and read the HTML file using BeautifulSoup
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        # Extract teacher name from the title
        teacher_name = soup.title.text.split('-')[-1].strip()
        
        # Find all rows
        rows = soup.find_all('tr')
        videos = []

        for row in rows:
            td_elements = row.find_all('td')
            if len(td_elements) == 0:
                continue

            # Extract video title
            title = td_elements[0].text.strip()

            # Extract download and PDF links
            download_button = row.find('button', class_='download-btn')
            pdf_button = row.find('button', class_='pdf-btn')

            download_link = download_button['onclick'].split("'")[1] if download_button else 'NONE'
            pdf_link = pdf_button['onclick'].split("'")[1] if pdf_button else 'NONE'

            # Check if the link contains 'NONE' and replace it with 'https://t.me/HIDEUC'
            if 'NONE' in download_link:
                download_link = 'https://i.ibb.co/4Ng0nk7/6717abd0.jpg'
            if 'NONE' in pdf_link:
                pdf_link = 'https://i.ibb.co/4Ng0nk7/6717abd0.jpg'

            # Append both download and PDF links with the teacher's name to the list
            videos.append(f"{title} {teacher_name}: {download_link}")
            videos.append(f"{title} {teacher_name}: {pdf_link}")

    # Create a text file to save the extracted data
    txt_file = os.path.splitext(html_file)[0] + '.txt'
    with open(txt_file, 'w') as f:
        f.write('\n'.join(videos))

    # Send the text file as a reply
    await m.reply_document(document=txt_file, caption="Le Gand me Dable BSDK 😡\nWords By - 𝗛𝗔𝗖𝗞𝗛𝗘𝗜𝗦𝗧")
    
    # Remove the local text file after sending it
    os.remove(txt_file)

@bot.on_message(filters.command(["op"]))
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

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend the index from where you want to start downloading (default is 1)")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send /d for using the filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '/d':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter Your Name like `HACKHEIST` or send `op` to use the default**")
    input15: Message = await bot.listen(editable.chat.id)
    raw_text15 = input15.text
    await input15.delete(True)
    OP = raw_text15 if raw_text15 != 'op' else "️ ⁪⁬⁮⁮⁮"

    await editable.edit("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)

    resolution_map = {
        "144": "256x144",
        "240": "426x240",
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080"
    }
    res = resolution_map.get(raw_text2, "UN")

    await editable.edit("**Enter Your Tag like `[@TEAM_OPTECH]` or send `de` for default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    MR = raw_text3 if raw_text3 != 'de' else "️ ⁪⁬⁮⁮⁮"

    await editable.edit("**Enter Your Website URL ☠️ or send `WEB` for default**")
    input8: Message = await bot.listen(editable.chat.id)
    raw_text8 = input8.text
    await input8.delete(True)
    WEB = raw_text8 if raw_text8 != 'WEB' else "https://i.ibb.co/W6d91vd/66f7961e.jpg"

    await editable.edit("**Send the thumbnail URL or enter `no` for none**")
    input6: Message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    thumb = raw_text6

    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    # Ask for the token once at the beginning of the command
    token = await bot.ask(m.chat.id, "Please provide your token:")
    token_value = token.text  # Store the token value

    count = int(raw_text) if len(links) > 1 else 1

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}',
                                   headers={'x-access-token': 'YOUR_ACCESS_TOKEN'}).json()['url']

            elif '/master.mpd' in url:
                # Use the stored token for all relevant URLs
                id = url.split("/")[-2]
                url = f"https://pwapi-aaebd595f347.herokuapp.com/pw-dl/{id}/master.m3u8&token={token_value}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "@").replace("*", "").replace(".", "").replace("https", "").replace("http", "").replace("NONE", "https://t.me/HIDEUC").strip()                                                        
            name = f'{OP} {MR} {name1[:60]}'                                                        
                                                        
            if "youtu" in url:                                                        
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"                                                        
            else:                                                        
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"                                                        
                                                        
            if "jw-prod" in url:                                                        
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'                                                        
            else:                                                        
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'                                                        
                                                        
            try:                                                          
                                                                        
                cc = f'**{name1} {MR}.mkv**\n\n**❃ 𝗕𝗮𝘁𝗰𝗵 » {b_name}**\n\n**♛ 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝔼𝔻 𝔹𝕐 ★ {MR}**\n**━━━━━━━✦✗✦━━━━━━━**\n**{WEB}**'
                cc1 = f'**{name1} {MR}.pdf**\n\n**❃ 𝗕𝗮𝘁𝗰𝗵 » {b_name}**\n\n**♛ 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝔼𝔻 𝔹𝕐 ★ {MR}**\n**━━━━━━━✦✗✦━━━━━━━**\n**{WEB}**'
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
                        continue                                                        
                                                                        
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
                        continue                                                        
                else:                                                        
                    Show = f"**⥥ 📥 ＤＯＷＮＬＯＤＩＮＧ 📥 :-**\n\n**📝Name »** `{name}\n❄𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**Url :-** `Kya karega URL dekhke ☠️☠️`\n\n **Bot made by {MR} (Daddy)🧑🏻‍💻**"                                                        
                    prog = await m.reply_text(Show)                                                        
                    res_file = await helper.download_video(url, cmd, name)                                                        
                    filename = res_file                                                        
                    await prog.delete(True)                                                        
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)                                                        
                    count += 1                                                        
                    time.sleep(1)                                                        
                                                        
            except Exception as e:                                                        
                await m.reply_text(                                                        
                    f"**Failed to Download/Extract 😫**\n\n**Name** - {cc}\n**𝗟𝗜𝗡𝗞** - {url}\n\nSorry {MR} 🙏**"                                                        
                )                                                        
                continue                                                        
                                                        
    except Exception as e:                                                        
        await m.reply_text(e)                                                        
    await m.reply_text("**Done✅**")                                                        
                                                        
                                                        
bot.run()                                                        
                                                        

                                                        
                                                        
                                                        
