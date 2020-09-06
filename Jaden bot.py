import discord
import os
from discord.ext import commands


client = commands.Bot(command_prefix = '-')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity = discord.Streaming(name = 'Type -commands for commands!', url = 'https://www.twitch.tv/savagepatchboy'))
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 648362981721374723:
        client.load_extension(f'cogs.{extension}')
        await ctx.send('Cog loaded')
    
    else:
        await ctx.send("This is an bot owner only command")

@client.command()
async def cogs(ctx):
    if ctx.author.id == 648362981721374723:
        
        em = discord.Embed( 
            title='Cogs',
            description='commands - **Contains commands command**\nLeveling - **Contains leveling system**\ntextcmds - **Contains text based commands**',
            colour = discord.Colour.orange()
        )
        await ctx.send('', embed=em)
    
    else:
        await ctx.send('Only the bot owner can access this command!')

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 648362981721374723:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog unloaded')
    
    else:
        await ctx.send("This is an bot owner only command!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzEwOTcxMTU5ODA5ODg0MjMx.Xr8NfQ.qNBwkmvGNUJ8U-O3TwIJ1Hx2Ewk")
