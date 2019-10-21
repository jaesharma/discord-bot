import discord
from discord.ext import commands

TOKEN='NjM1MTk2MDk1MDM4NzUwNzUw.Xatixw.5bbJMgRmlpF9CcEx6hUQZTWjHnY'

client=commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('bot is ready')

@client.command()
async def echo(channel,arg):
	await channel.send('returned')

@client.command(pass_context=True)
async def clear(ctx,amount=100):
	channel=ctx.message.channel
	msgs=[]
	async for msg in client.logs_from(channel,limit=100):
		msgs.append(msg)
	await client.delete_messages(messages)
	await channel.send('messages deleted')

client.run(TOKEN)