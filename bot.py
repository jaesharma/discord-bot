import discord
from discord.ext import commands
import asyncio
import youtube_dl
import time
import os
from datetime import datetime as dt
from gtts import gTTS as gtts
import praw

#secrets:
TOKEN="TOKEN"
client_id='client_id'
client_secret='client_secret'
user_agent="bru"

player={}

bclient=commands.Bot(command_prefix='.')

async def memes():
	while True:
		reddit=praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)
		sub=reddit.subreddit('memes').new(limit=900)
		channels = bclient.get_all_channels()
		for channel in channels:
			if channel.name=='memes':
				channel=bclient.get_channel(channel.id)
				for i in sub:
					await channel.send(i.url)
					await asyncio.sleep(300)
		await asyncio.sleep(30)


async def dank():
	while True:
		reddit=praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)
		sub=reddit.subreddit('dankmemes').new(limit=900)
		channels = bclient.get_all_channels()
		for channel in channels:
			if channel.name=='memes':
				channel=bclient.get_channel(channel.id)
				for i in sub:
					await channel.send(i.url)
					await asyncio.sleep(300)
		await asyncio.sleep(30)

bclient.loop.create_task(dank())
bclient.loop.create_task(memes())

@bclient.event
async def on_ready():
    print('Logged in as')
    print(bclient.user.name)
    print(bclient.user.id)

@bclient.event
async def on_message(message):
	print('bclient has sent a message')
	await bclient.process_commands(message)

@bclient.command(pass_context=True)
async def clear(ctx,amount=100):
	channel=ctx.message.channel
	msgs=[]
	async for msg in bclient.logs_from(channel,limit=100):
		msgs.append(msg)
	await bclient.delete_messages(messages)
	await channel.send('messages deleted')

@bclient.command(pass_context=True)
async def reddit(ctx,*args):
	channel=ctx.message.channel
	count=0

	reddit=praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)

	sub=reddit.subreddit(args[0]).new(limit=int(args[1]))

	for i in sub:
		url=i.url
		if count is args[1]:
			break
		if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
			await channel.send(url)
		else:
			await channel.send(i.title)
			await channel.send('---------------')
		count+=1

#audio player
@bclient.command(pass_content=True)
async def say(ctx,*,text):
	message=gtts(text)
	message.save('tts.mp3')
	channel=ctx.message.channel
	user=ctx.message.author
	if user.voice is None:
		await channel.send('Join a voice channel first')
		return
	voice_channel=user.voice.channel
	try:
		voice_client = await voice_channel.connect()
	except:
		pass
	ctx.guild.voice_client.play(discord.FFmpegPCMAudio('tts.mp3'))
	

@bclient.command(pass_content=True)
async def q(ctx):
	await bclient.logout()

bclient.run(TOKEN)

