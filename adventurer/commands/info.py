import disnake
from disnake.ext import commands

class Info(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Info(bot))
    print("Loaded Bot Information!")