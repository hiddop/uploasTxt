from pyrogram import Client, filters
import os
import subprocess

bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

DEFAULT_THUMBNAIL = "https://i.ibb.co/dPpqpdP/67178015.jpg"
DEFAULT_RESOLUTION = "480"

@bot.on_message(filters.command("download"))
async def download_command(bot: Client, message):
    try:
        # Ask for Name and URL
        await message.reply_text("**Enter Name and URL in the format:**\n`Name: URL`")
        input_msg = await bot.listen(message.chat.id)
        input_text = input_msg.text
        await input_msg.delete()

        # Validate input
        if ":" not in input_text:
            await message.reply_text("Invalid format! Please use `Name: URL`.")
            return

        name, url = map(str.strip, input_text.split(":", 1))
        if not name or not url:
            await message.reply_text("Name or URL cannot be empty!")
            return

        # Set defaults for thumbnail and resolution
        thumbnail = DEFAULT_THUMBNAIL
        resolution = DEFAULT_RESOLUTION

        # Download using yt-dlp
        await message.reply_text(f"Starting download for:\n**Name:** {name}\n**URL:** {url}\n**Resolution:** {resolution}\n**Thumbnail:** {thumbnail}")
        cmd = f'yt-dlp -o "{name}.mp4" -f "best[height<={resolution}]" "{url}"'
        subprocess.run(cmd, shell=True)

        # Check if file exists
        if os.path.exists(f"{name}.mp4"):
            await message.reply_video(
                video=f"{name}.mp4",
                caption=f"**Downloaded:** {name}",
                thumb=thumbnail
            )
            os.remove(f"{name}.mp4")
        else:
            await message.reply_text("Failed to download the video.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

bot.run()
