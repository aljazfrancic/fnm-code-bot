import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + " reporting for duty!")
    #print(str(client.guilds))
    #for guild in client.guilds:
    #    print(guild.channels)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    command = "!fnm-code-bot-deploy"
    
    if message.content[:len(command)] == command:
        await message.channel.send("Roger, roger!")
        
        input = message.content.split()
        
        target_channel = input[1]
        fnmcodes = input[2:]
        print(target_channel, fnmcodes)
        
        #MTG Slovenia Discord guild id
        #691942331091517530
        
        #commander guild id
        #760280589244563487
        
        #sad-bot's sad server guild id
        #804097685871132702
        
        guild = client.get_guild(760280589244563487) #TODO GET THIS CODE FROM MESSAGE FOR PORTABILITY
        
        for chan in guild.channels:
            if chan.name == target_channel:
                posts = await chan.history().flatten()
                senders = []
                for post in posts:
                    senders.append(post.author)
                senders = list(set(senders))
                senders.reverse()
                print(senders)
                for i, member in enumerate(senders):
                    if i >= len(fnmcodes):
                        await message.channel.send("Zmanjkalo je kod za " + member.name + "!")
                    await member.create_dm()
                    await member.dm_channel.send(fnmcodes[i])
                    await message.channel.send("Koda " + fnmcodes[i] + " poslana " + member.name + "!")
                await chan.send("Kode so bile poslane!")
                break
            

        
        
client.run(TOKEN)