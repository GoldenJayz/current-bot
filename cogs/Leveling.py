import discord
from discord.ext import commands

import json

import asyncio


class Leveling(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open(r"C:\Users\jmdan\OneDrive\Desktop\Current Discord Bot files\cogs\users.json", 'r') as f:
            self.users = json.load(f)
    
    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open(r"C:\Users\jmdan\OneDrive\Desktop\Current Discord Bot files\cogs\users.json", 'w') as f:
                json.dump(self.users, f, indent=4)
            
            await asyncio.sleep(5)
    
    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False
   
   
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        author_id = str(message.author.id)

        if author_id in  self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0
        
        self.users[author_id]['exp'] += 1

        if self.lvl_up(author_id):
            await message.channel.send(f"{message.author.mention} you are now level {self.users[author_id]['level']}")
    

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("You have no level.")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"Level - {member}", icon_url=self.client.user.avatar_url)

            embed.add_field(name="Level", value=self.users[member_id]['level'])
            embed.add_field(name="XP", value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)
            

def setup(client):
    client.add_cog(Leveling(client))
