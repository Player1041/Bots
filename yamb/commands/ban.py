import disnake
from disnake.ext import commands

class Ban(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ban(self, inter, member: disnake.Member, reason: str = None):
        """
        Bans a member.
        
        Parameters
        ----------
        
        member: The member you want to ban.
        reason: Shows in audit logs (optional).
        """
def setup(bot):
    bot.add_cog(Ban(bot))
    print("Loaded Ban Management")