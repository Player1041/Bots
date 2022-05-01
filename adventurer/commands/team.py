import disnake
from disnake.ext import commands

TeamOpt = commands.option_enum({
    "Professional", "pro",
    "Competitive": "comp",
    "Base": "base"
})

class Team(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
        async def team(self, inter):
            pass
    
    @team.sub_command()
    async def assign(self, inter, member: disnake.Member, team: TeamOpt):
            """Allows for team assigning.
            
            Parameters
            ----------
            member: The member being assigned a team.
            team: The team you are assigning.
            """
            embed = disnake.Embed(
                name = f"Assignment {status}",
                description = description
                )
            
            

def setup(bot):
    bot.add_cog(Team(bot))
    print("Loaded Team Management!")