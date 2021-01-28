import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
command = "!fnm-code-bot-deploy"

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
    
    if message.content[:len(command)] == command:
        await message.channel.send("Roger, roger!")
        
        input = message.content.split()
        
        #MTG Slovenija guild id
        #691942331091517530
        
        #Commander guild id
        #760280589244563487
        
        #sad-bot's sad server guild id
        #804097685871132702
        
        guild_id = input[1]
        target_channel = input[2]
        fnm_codes = input[3:]
        
        print(guild_id, target_channel, fnm_codes)
        
        guild = client.get_guild(int(guild_id))
        
        for chan in guild.channels:
            if chan.name == target_channel:
                posts = await chan.history().flatten()
                senders = []
                for post in posts:
                    if post.attachments:
                        senders.append(post.author)
                senders = list(set(senders))
                senders.reverse()
                for i, member in enumerate(senders):
                    if i >= len(fnm_codes):
                        await message.channel.send("Ran out of codes for " + member.name + "!")
                    else:
                        await member.create_dm()
                        await member.dm_channel.send("`" + fnm_codes[i] + "`")
                        await message.channel.send("Code `" + fnm_codes[i] + "` sent to " + member.name + "!")
                await chan.send("Kode so bile poslane!")
                break
                
client.run(TOKEN)