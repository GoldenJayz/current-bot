import discord
from discord.ext import commands

client = discord.Client()

class commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def commands(self, ctx):
        em = discord.Embed( 
            title='Commands',
            description='A simple list of commands',
            colour = discord.Colour.orange()
        )
        em.add_field(name='**Fun/Games**', value='-8ball\n-shoot', inline=True)
        em.add_field(name='**Anime Gifs**', value='-nezukogif\n-nezukorunningmeme\n-jojo\n-demonslayer', inline=True)
        em.add_field(name='**Misc.**', value='-clear', inline=False)
        em.set_footer(text='Thanks for utilizing my bot ^-^')
        em.set_author(name='Jadek#9012',
        icon_url='https://cdn.discordapp.com/avatars/648362981721374723/d9e5e0da3ee56c15156e08e6d06c685f.png?size=256')
        em.set_image(url='https://cdn.discordapp.com/attachments/742148980682784793/751764081081581568/asuna.png')

        await ctx.send('', embed=em)
    
def setup(client):
    client.add_cog(commands(client))