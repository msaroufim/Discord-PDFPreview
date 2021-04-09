# Work with Python 3.6
import discord
import requests
import pdf2image
import math
import os
# import io

TOKEN = 'ODMwMDc4NzkyODMwNTUwMDQ2.YHBdHg.mrFTPTza3yPpQ7ACPYsJJBMYa7M'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!pdfcheck'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.endswith('.pdf'):
        pdf = requests.get(message.content)
        screenshots = pdf2image.convert_from_bytes(pdf.content)
        outputs = [] 
        for i in range(0, min(len(screenshots), 4)):  
            screenshots[i].save("screenshot.png", filename="screenshot.png")
        
            await message.channel.send(file=discord.File('screenshot.png'))
            os.remove("screenshot.png")

    if message.attachments[0].url.endswith(".pdf"):
        pdf = requests.get(message.attachments[0].url)
        screenshots = pdf2image.convert_from_bytes(pdf.content)
        outputs = [] 
        for i in range(0, min(len(screenshots), 4)):  
            screenshots[i].save("screenshot.png", filename="screenshot.png")
        
            await message.channel.send(file=discord.File('screenshot.png'))
            os.remove("screenshot.png")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)


