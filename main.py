# Work with Python 3.6
import discord
import requests
import pdf2image
import io

TOKEN = 'NTkwNjM2ODUwNjEyMjczMTYz.XQlIxg.vdQaTJXSRzt1PbGYCpXOJD_5b80'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('.pdf'):
        pdf = requests.get(message.content)

        #slideshow sounds awesome actually
        ## should only get the first image, getting entire pdf is kinda dumb
        screenshot = pdf2image.convert_from_bytes(pdf.content)[0]
        screenshot.save("screenshot.png", filename="screenshot.png")
        
        await client.send_file(message.channel, "screenshot.png")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)


