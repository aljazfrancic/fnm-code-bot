import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + " reporting for duty!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    command = "!fnm-code-bot-deploy"
    
    if message.content[:len(command)] == command:
        await message.channel.send("Roger, roger!")
        
        input = message.content.split()
        
        channel = input[1]
        fnmcodes = input[2:]
        print(channel, fnmcodes)
        
client.run(TOKEN)