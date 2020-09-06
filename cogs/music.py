import discord
from discord.ext import commands

client = discord.Client()

class commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def music(self, ctx):
        await ctx.send("Music Cog is working!")
        
    
def setup(client):
    client.add_cog(commands(client))