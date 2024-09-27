import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from aiohttp import ClientSession
import helper
import time
import os
import re
from subprocess import getstatusoutput

bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@bot.on_message(filters.command(["start"]))
async def start(bot, m: Message):
    await m.reply_text(f"Hello {m.from_user.first_name}, I am a TXT file Downloader Bot.")

@bot.on_message(filters.command(["hackheist"]))
async def handle_txt(bot, m: Message):
    editable = await m.reply_text('Send TXT file for download:')
    input: Message = await bot.listen(editable.chat.id)

    # Check if the message contains downloadable media
    if input.document or input.video or input.photo or input.audio:
        # Download the file
        x = await input.download()
        await input.delete(True)
    else:
        await m.reply_text("This message doesn't contain any downloadable media.")
        return

    # Processing the file
    try:
        with open(x, "r") as f:
            content = f.read()
        links = content.split("\n")
        os.remove(x)
    except Exception as e:
        await m.reply_text(f"Invalid file input or error reading file: {e}")
        os.remove(x)
        return

    # Fetching details
    await editable.edit(f"Total links found: {len(links)}. From which link should the download start? Default is 1.")
    input_start: Message = await bot.listen(editable.chat.id)
    start_idx = int(input_start.text) - 1
    await input_start.delete(True)

    await editable.edit("Enter resolution (144, 240, 360, 480, 720, 1080):")
    input_res: Message = await bot.listen(editable.chat.id)
    raw_res = input_res.text
    await input_res.delete(True)

    resolutions = {
        "144": "256x144",
        "240": "426x240",
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080"
    }
    res = resolutions.get(raw_res, "UN")

    await editable.edit("Now send the **Thumbnail URL** or type `no` for no thumbnail:")
    input_thumb = await bot.listen(editable.chat.id)
    thumb_url = input_thumb.text
    await input_thumb.delete(True)

    thumb = None
    if thumb_url.lower() != "no":
        getstatusoutput(f"wget '{thumb_url}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"

    await editable.edit("Enter a custom caption for the downloads and uploads:")
    input_caption: Message = await bot.listen(editable.chat.id)
    custom_caption = input_caption.text
    await input_caption.delete(True)

    await editable.edit("Starting download...")

    # Downloading process
    for i in range(start_idx, len(links)):
        url = links[i].strip()

        if not url.startswith("http"):
            continue

        name = f"video_{i+1}.mp4"  # Dynamic file name

        if "youtu" in url:
            ytf = f"b[height<={raw_res}][ext=mp4]/bv[height<={raw_res}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
        else:
            ytf = f"b[height<={raw_res}]/bv[height<={raw_res}]+ba/b/bv+ba"

        cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}"'

        try:
            if url.endswith(".pdf"):
                cmd = f'yt-dlp -o "{name.replace(".mp4", ".pdf")}" "{url}"'
                os.system(cmd)

                if thumb:
                    await bot.send_document(m.chat.id, document=f'{name.replace(".mp4", ".pdf")}', thumb=thumb, caption=f"{custom_caption} (Downloaded PDF: {name.replace('.mp4', '.pdf')})")
                else:
                    await bot.send_document(m.chat.id, document=f'{name.replace(".mp4", ".pdf")}', caption=f"{custom_caption} (Downloaded PDF: {name.replace('.mp4', '.pdf')})")

            else:
                os.system(cmd)
                if thumb:
                    await bot.send_video(m.chat.id, video=name, thumb=thumb, caption=f"{custom_caption} (Downloaded Video: {name})")
                else:
                    await bot.send_video(m.chat.id, video=name, caption=f"{custom_caption} (Downloaded Video: {name})")

            time.sleep(1)  # Prevent flooding

        except FloodWait as e:
            await m.reply_text(f"FloodWait: Sleeping for {e.x} seconds.")
            time.sleep(e.x)
            continue
        except Exception as e:
            await m.reply_text(f"Error downloading {url}: {e}")
            continue

    await m.reply_text("Download completed.")
    await editable.delete()

bot.run()
