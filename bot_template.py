import os
import discord
from random import choice  
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is open for business!') 

@client.event 
async def on_member_join():
    await member.create_dm()
    await member.dm_channel.send()
    await member.dm_channel.send(f'Introducing the one and only, {member.name}!')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.lower() == "sorry":
        response = f"Don't apologise!, {message.author}!"
        await message.channel.send(response)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

    if message.content.lower() == "when?": 
        response = f"Do it on {choice(days)}!"
        await message.channel.send(response) 

client.run(TOKEN)
