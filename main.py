# Work with Python 3.6
import discord
import requests
import pdf2image
# import io

TOKEN = 'NTkwNjM2ODUwNjEyMjczMTYz.XQlHbg.JgrsW4JrwIz7jGszCyW-8H10pXU'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('.pdf') and 'arxiv' in message.content:
        pdf = requests.get(message.content)
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


