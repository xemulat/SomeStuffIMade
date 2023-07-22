# require 'message_content' intent
# require 'settings.AVB.json' file 

import disnake as discord
from json import load

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'volx' in message.content and 'hate' in message.content:
        await message.channel.send('I HATE VOLX TOO!!')

with open('settings.AVB.json', 'r') as f:
    g = load(f)
    token = g["Token"]
client.run(token)
