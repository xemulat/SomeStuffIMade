from disnake import Intents, Game, CommandInteraction, Member, Embed, utils
from disnake.ext.commands import InteractionBot, CommandSyncFlags, Param
from typing import List
from datetime import datetime, timedelta

import asyncio

import hashlib


from os import listdir
from os.path import join, isfile

# Set vars
# Target folder for mixtapes (lighttpd server)
folder_path = "/home/xem/Pulpit/xemulated/files/mixtapes"

# Target videos for the drive playlist
drivePlaylist = "https://www.youtube.com/playlist?list=PLPKhAsFCbjbX0YWpRpmCamuuyxOdUvN3c"

def convertDateToPLTime(date):
    date_str = str(date)
    date = datetime.fromisoformat(date_str[:-6])  # Remove the timezone information

    # Add 2 hours to the given date
    result_date = date + timedelta(hours=2)

    # Convert the result_date to ISO 8601 format
    result_date_str = result_date.strftime("%Y-%m-%d %H:%M:%S.%f") + "+00:00"

    return(result_date_str)

def sha1Hasher(data):
    # Implementation of SHA-1 hash calculation using the built-in hash() function
    h = hashlib.new('sha1')
    h.update(data)
    return h.hexdigest()

def getFilesInADirectory():
    file_names = []
    for file_name in listdir(folder_path):
        if isfile(join(folder_path, file_name)):
            file_names.append(file_name)
    return file_names

async def autocompleteMixtapes(inter, string: str) -> List[str]:
    string = string.lower()
    return [i for i in getFilesInADirectory() if string in i.lower()]

command_sync_flags = CommandSyncFlags.default()
command_sync_flags.sync_commands = True
intents = Intents.default()
intents.message_content = True
intents.voice_states = True
activity = Game(name='say gex')
bot = InteractionBot(asyncio_debug=True, intents=intents, command_sync_flags=command_sync_flags, activity=activity)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.slash_command()
async def mixtapeplay(inter: CommandInteraction, mixtape: str = Param(autocomplete=autocompleteMixtapes)):
    voice_state = inter.author.voice
    if voice_state and voice_state.channel:
        channel = voice_state.channel
        voice_client = await channel.connect()
        await inter.send(f'-play http://localhost/files/mixtapes/{mixtape.replace(" ", "%20")}')
        await asyncio.sleep(2)
        await voice_client.disconnect()

        await inter.delete_original_message()  # Remove the original message
    else:
        await inter.response.send_message("You aren't connected to a voice channel!")

@bot.slash_command()
async def driveplay(inter: CommandInteraction, loopqueue: bool = True):
    voice_state = inter.author.voice
    if voice_state and voice_state.channel:
        channel = voice_state.channel
        voice_client = await channel.connect()
        print(f"DEBUG: Inputting the playlist into the queue...")
        await inter.send(f'-play {drivePlaylist}')
            
        if loopqueue == True:
            await asyncio.sleep(3)
            await inter.send('-loop')
            await asyncio.sleep(2)
            await inter.send('-loop')

        await voice_client.disconnect()

        await inter.delete_original_message()
    else:
        await inter.response.send_message("You aren't connected to a voice channel!")



bot.run("token.token.token")
