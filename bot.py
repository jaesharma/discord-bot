import discord
from discord.ext import commands
import asyncio
import time
from datetime import datetime as dt
import praw
import secrets

TOKEN=secrets.gettoken()

client=commands.Bot(command_prefix='.')


async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channels = client.get_all_channels()
    for channel in channels:
    	if channel.name=='general':
    		channel=client.get_channel(channel.id)
    		break
    while True:
    	if 9<dt.now().hour<10:
    		print('schedule now')
    	await asyncio.sleep(10)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.loop.create_task(my_background_task())

@client.event
async def on_message(message):
	print('client has sent a message')
	await client.process_commands(message)

@client.command()
async def echo(channel,arg):
	await channel.send('none')

@client.command()
async def repeat(channel,*args):
	output=''
	for word in args:
		output+=word
		output+=' '
	await channel.send(output)

@client.command(pass_context=True)
async def clear(ctx,amount=100):
	channel=ctx.message.channel
	msgs=[]
	async for msg in client.logs_from(channel,limit=100):
		msgs.append(msg)
	await client.delete_messages(messages)
	await channel.send('messages deleted')

@client.command(pass_context=True)
async def reddit(ctx,*args):
	channel=ctx.message.channel
	client_id=secrets.getuser()
	client_secret=secrets.getsecret()
	user_agent="bru"
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


client.run(TOKEN)