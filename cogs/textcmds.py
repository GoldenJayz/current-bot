import discord
from discord.ext import commands
import random

client = discord.Client()

class textcmds(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command(aliases=['8ball'])
    async def ball(self, ctx):
        randomlist = ['Maybe','Yes','No',]
        randomgif = ['https://media3.giphy.com/media/141iprzbEPjCiQ/giphy.gif', 'https://i.imgur.com/akdtE4H.gif', 'https://thumbs.gfycat.com/QuestionableMajesticBillygoat-small.gif',]
        em = discord.Embed(
            title="The magic 8 ball has spoken.",
            description=(random.choice(randomlist)),
            colour = discord.Colour.blurple()
        )
        em.set_image(url= (random.choice(randomgif)))
        await ctx.send(embed=em)
    
    @commands.command()
    async def demonslayer(self, ctx):
        randomlist = ['https://media.giphy.com/media/VEzYdo930nTiTuVeMU/giphy.gif',  'https://media.giphy.com/media/J6JazAkCVLId91L4yM/giphy.gif', 'https://media.giphy.com/media/Yq1tXTNe5PDdQEhKXG/giphy.gif', 'https://media.giphy.com/media/TgyJebqyMtPrOxiPdk/giphy.gif', 'https://media.giphy.com/media/f7k6TfAFkiAqKVcJGH/giphy.gif', 'https://media.giphy.com/media/JrHB5IyuBzKwPEPZe4/giphy.gif', 'https://media.giphy.com/media/H83c2x0NWvFhtgK4V2/giphy.gif', 'https://media.giphy.com/media/ZaueN0ipnurQlgKsRu/giphy.gif', 'https://media.giphy.com/media/dVcrkGH9DU9EpdGsV8/giphy.gif']
        em = discord.Embed(
            title='Demon Slayer Gif!',
            description=':)',
            colour = discord.Colour.purple()
        )
        em.set_image(url= (random.choice(randomlist)))
        await ctx.send(embed=em)
    
    @commands.command()
    async def jojo(self, ctx):
        randomlist = ['https://media.giphy.com/media/h7FZESJ1Ter5bGhUDG/giphy.gif',  'https://thumbs.gfycat.com/ForthrightBoldDaddylonglegs-max-1mb.gif', 'https://media.giphy.com/media/f9jxYYRVPHtKsCf9sy/giphy.gif']
        em = discord.Embed(
            title='Here is your Jojo gif.',
            description=':)',
            colour = discord.Colour.purple()
        )
        em.set_image(url= (random.choice(randomlist)))
        await ctx.send(embed=em)
    
    @commands.command()
    async def shoot(self, ctx):
        em = discord.Embed(
            title='You have been shot!',
            description='You have a gun shot in your chest',
            colour = discord.Colour.green()
        )
        em.set_image(url='https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif')
        await ctx.send('', embed=em)

    
def setup(client):
    client.add_cog(textcmds(client))