import disnake
from disnake.ext import commands

class Ban(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Ban(bot))
    print("Loaded Ban Management!")