import disnake
from disnake import commands

class Info(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def serverinfo(self, inter, server: int = 