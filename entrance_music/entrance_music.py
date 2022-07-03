from redbot.core import commands
import discord

class entrance_music(commands.Cog):
    """Plays themes using the Theme cog upon a user joining a voice channel"""

    def __init__(self, bot):
        self.bot = bot

    async def Entrance(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")