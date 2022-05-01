import disnake
from disnake.ext import commands

class Role(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Role(bot))
    print("Loaded Role Management!")