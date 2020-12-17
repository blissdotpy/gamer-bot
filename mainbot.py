import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!', description='Gamers only')
TOKEN = 'NzQxMzc2ODMzMTAyMDIwNzQw.Xy2q-w.t3Xws0cb6Y2439SIDdVWqRFfy8k'


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with the boys'))                                    
    print("Bot is online")

@client.event
async def on_ready(ctx):
    await ctx.send(f"Happy Holidays Gamers.")

@client.command()
async def gamers(ctx, member : discord.Member):
    #usman = '<@#7860>'
    await ctx.send(f"Gamer time {member.member}")

@client.command()
async def gn(ctx):
    await ctx.send('Goodnight gamers')

@client.command()
async def gamertime(ctx):
    await ctx.send("It's gamer time")

@client.command()
async def botnotbroke(ctx):
    await ctx.send('This bot isnt broken')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello! {ctx.message.author.mention}')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def report(ctx,*,report):
    print(f'Report : {report}')
    await ctx.send(f'Sent your report : ({report}) to server Admin')
    print(f' ID:{ctx.message.author.mention}')

@client.command()
async def test(ctx, *args):
    embed = discord.Embed(title="This is a test", description="```HTTP\nThis is text```", color=0xFFFFFF)
    await ctx.send(embed=embed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f"{member} banned from server")
    await ctx.send(f' ID: {ctx.message.author.mention}')

@client.command()
async def speed(ctx):
    await ctx.send(f"Your Connection's download speed is: {round((st.download() / 1000000), 2)} Mbps")
    await ctx.send(f"Your connection's upload speed is: {round((st.upload() / 1000000), 2)} Mbps")

client.run(TOKEN)
