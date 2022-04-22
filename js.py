#we need to make the bot smarter. This means adding chat interactions and also a claim timer so that we don't draw suspicion with too many claims.
import discord
import time
import asyncio
from functions import claimCheck
client = discord.Client(self_bot = True)

channel = False
t = 0

@client.event
async def on_ready():
    print('online')

@client.event
async def on_message(message):

    global channel
    global t

    if message.author.id == 'Put your ids here':

        if message.content.startswith('$w') or message.content.startswith('$h'):  #if michael rolls
            channel = message.channel.id

            #activate the channel and claim all rolls for 3 seconds.
            
            t = time.time()
    
    elif channel == message.channel.id and message.author.id == 432610292342587392 and message.embeds: #if it appears to be a roll in the correct channel
        
        if time.time() - t < 3:

            footer = message.embeds[0].footer.text

            if footer != discord.Embed.Empty: 

                if 'Belongs' in footer: #it is a claimed character (most of the time)

                    #react to all reactions on it(can have error, but will be rare)

                    print('kakera??')

                    await asyncio.sleep(0.8)

                    for i in message.reactions:
                        
                        i = i.emoji
                        await message.add_reaction(i)

                else:

                    #the footer was something else like you are running out of rolls, check to claim

                    await claimCheck(message)

            else:#no footer, but could still be claimable

                await claimCheck(message)

client.run('put bot token here')