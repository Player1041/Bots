import disnake
from disnake.ext import commands


class Roles(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    async def role(self, inter):
        pass
    
    @role.sub_command()
    async def add(self, inter, role: disnake.Role, member: disnake.Member, reason: str = None):
        """
        Assigns a role to a member.
        
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
            title = "Role failed to assign: Hierarchy Error",
            description = f"You ({inter.author.mention} / {inter.author}) have a role lower than {role.mention}. Get a higher role and try again."
            )
        botRoleEmbed = disnake.Embed(
            title = "Role failed to assign: Bot Role",
            description = f"You ({inter.author.mention} / {inter.author}) have tried to assign a bot managed role. Select a different role and try again."
            )
        selfPermsEmbed = disnake.Embed(
            title = "Role failed to assign: Missing Permissions",
            description = f"You ({inter.author.mention} / {inter.author}) have not got the `Manage Roles` permission. Get the `Manage Roles` permission and try again."
            )
        botPermsEmbed = disnake.Embed(
            title = "Role failed to assign: Missing Permissions",
            description = f"I have not got the `Manage Roles` permission. Give me the `Manage Roles` permission and try again."
            )
        if not inter.guild.me.guild_permissions.manage_roles:
            return await inter.response.send_message(embed = botPermsEmbed)
        if not inter.author.guild_permissions.manage_roles:
            return await inter.response.send_message(embed = selfPermsEmbed)
        if inter.author.top_role < role:
            return await inter.response.send_message(embed = failHeirEmbed)
        if not role.is_assignable():
            return await inter.response.send_message(embed = botRoleEmbed)
        await member.add_roles(role, reason=f": {reason}")
        await inter.response.send_message(embed = roleEmbed)
    
    
def setup(bot):
    bot.add_cog(Roles(bot))
    print("Loaded Role Management.")