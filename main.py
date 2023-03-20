import discord
import requests
import pdf2image
import re
import io
from PIL import Image
import datetime
import os

TOKEN = os.environ["DISCORD_BOT_TOKEN"]

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)

# Helper function to resize the image
def resize_image(image, scale_percent):
    width, height = image.size
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    return image.resize((new_width, new_height))

# Helper function to extract PDF URL from arXiv abstract page
def get_arxiv_pdf_url(url):
    if "arxiv.org/abs/" in url:
        pdf_url = url.replace("arxiv.org/abs/", "arxiv.org/pdf/") + ".pdf"
        return pdf_url
    return None

@client.event
async def on_message(message):
    
    # We workaround the discord message caching so we can post the same message multiple times
    message.content = f"{message.content} {datetime.datetime.utcnow().isoformat()}"

    if message.author == client.user:
        return

    # Check if the bot is mentioned
    if client.user in message.mentions:

        pdf_pattern = r"(?P<url>https?://[^\s]+\.pdf)"
        match = re.search(pdf_pattern, message.content)

        if not match:
            arxiv_pattern = r"(?P<url>https?://arxiv\.org/abs/[^\s]+)"
            match = re.search(arxiv_pattern, message.content)
            if match:
                url = get_arxiv_pdf_url(match.group('url'))
                if url:
                    match = re.search(pdf_pattern, url)

        if match:
            try:
                url = match.group('url')
                pdf = requests.get(url)

                # Get the specified page number, default is 1
                page_number = 1
                page_pattern = r"page\s*(?P<page>\d+)"
                match_page = re.search(page_pattern, message.content)
                if match_page:
                    page_number = int(match_page.group('page'))

                # Get the specified resize percentage, default is 100
                resize_percentage = 100
                resize_pattern = r"resize\s*(?P<resize>\d+)"
                match_resize = re.search(resize_pattern, message.content)
                if match_resize:
                    resize_percentage = int(match_resize.group('resize'))

                screenshots = pdf2image.convert_from_bytes(pdf.content)

                if 0 < page_number <= len(screenshots):
                    image = screenshots[page_number - 1]

                    if resize_percentage != 100:
                        image = resize_image(image, resize_percentage)

                    buffer = io.BytesIO()
                    image.save(buffer, format="PNG")
                    buffer.seek(0)

                    await message.channel.send(file=discord.File(buffer, "screenshot.png"))

                else:
                    await message.channel.send("Invalid page number.")

            except Exception as e:
                print(e)
                await message.channel.send("Error processing PDF.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)