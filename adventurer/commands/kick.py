import disnake
from disnake.ext import commands

class Kick(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Kick(bot))
    print("Loaded Kick Management!")