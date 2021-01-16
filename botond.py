import os
import random
import discord
import asyncio

#create the connection

TOKEN = 'NzQwNjI1MTc4MTA2NTI3ODQ2.Xyru8g.XLz5Gs0215DvfQZdSjJwvhivN2M'
client = discord.Client()

async def removeBotond():
    g = client.guilds[0]
    for vc in g.voice_channels:
        for m in vc.members:
            if m.name == 'Ceratuth ᛋᛖᚱᚨᛏᚢᚦ':
                await m.move_to(None)
                print('1')
async def moveBotond():
    g = client.guilds[0]
    for vc in g.voice_channels:
        for m in vc.members:
            if m.name == 'Ceratuth ᛋᛖᚱᚨᛏᚢᚦ':
                await m.move_to(g.voice_channels[3])
                print('2')

szopatas = [removeBotond,moveBotond]

async def teszt():
    print('func')

async def m():
    await random.choice(szopatas)()
    await asyncio.sleep(10)
    await m()

@client.event
async def on_ready():
    await m()
        

client.run(TOKEN)

