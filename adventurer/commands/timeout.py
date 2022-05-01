import disnake
from disnake.ext import commands

class Timeout(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Timeout(bot))
    print("Loaded Timeout Management!")