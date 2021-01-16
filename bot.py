import os

import discord

#create the connection


TOKEN = 'NzQwNjI1MTc4MTA2NTI3ODQ2.Xyru8g.XLz5Gs0215DvfQZdSjJwvhivN2M'
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    global cn
    if message.author == client.user:
        return      
    if message.content == '$play':
        att = message.attachments
        if att.__len__() > 0:
            await att[0].save("music.mp3")
            source = discord.FFmpegPCMAudio('music.mp3')
            print(client.voice_clients)
            print(message.author.voice)
            if client.voice_clients.__len__() != 0:
                cn.play(source)
            if client.voice_clients.__len__() == 0 and message.author.voice != None:
                cn = await message.author.voice.channel.connect()
                cn.play(source)          
    
    if message.content == 'stop':
        print(cn)
        if cn != None:
            await cn.disconnect()




client.run(TOKEN)

