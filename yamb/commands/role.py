import disnake
from disnake.ext import commands


class Roles(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    async def role(self, inter):
        pass
    
    @role.sub_command()
    async def add(self, inter, roles: [role for role in guild.roles if role.is_assignable()], member: disnake.Member, reason: str = None):
        """Assigns a role to a member.
        
        Parameters
        ----------
        
        role: The role you want to assign.
        member: The member you want to assign to.
        reason: Shows in audit logs (optional).
        """
        roleEmbed = disnake.Embed(
            title = "Role Assigned",
            description = f"{role.mention} was assigned to {member.mention} / {member} by {inter.author.mention} / {inter.author}."
            )
        failHeirEmbed = disnake.Embed(
            title = "Role failed to assign: Heirarchy Error",
            description = f"You ({inter.author.mention} / {inter.author}) have a role lower than {role.mention}. Get a higher role and try again.")
        if inter.author.top_role < role:
            await inter.response.send_message(embed = failHeirEmbed)
        await member.add_roles(role, reason=f": {reason}")
        await inter.response.send_message(embed = roleEmbed)
    
    
def setup(bot):
    bot.add_cog(Roles(bot))
    print("Loaded Role Management.")