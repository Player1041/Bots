import disnake
from disnake.ext import commands
import os


class Kick(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def kick(self, inter, member: disnake.Member, reason: str = None):
        """
        Kicks a member.
        
        Parameters
        ----------
        member: The member you want to kick.
        reason: Displays in audit logs (optional)
        """
        kickEmbed = disnake.Embed(
            title = "Kicked Successfully",
            description = f"{inter.author.mention} / {inter.author} has successfully kicked {member} from the server.",
            colour = disnake.Colour.random()
            )
        permsEmbed = disnake.Embed(
            title = "Failed to Kick: Missing Permissions",
            description = f"You ({inter.author.mention} / {inter.author}) do not have the `Kick Members` permission. Get the `Kick Members` permission and try again.",
            colour = disnake.Colour.random()
            )
        selfPermsEmbed = disnake.Embed(
            title = "Failed to Kick: Missing Permissions",
            description = f"I do not have the `Kick Members` permission. Give me the `Kick Members` permission and try again.",
            colour = disnake.Colour.random()
            )
        hierEmbed = disnake.Embed(
            title = "Failed to Kick: Hierarchy Error",
            description = f"You ({inter.author.mention} / {inter.author}) do not have a role high enough to kick {member.mention} / {member}. Get a higher role and try again.",
            colour = disnake.Colour.random()
            )
        selfHierEmbed = disnake.Embed(
            title = "Failed to Kick: Hierarchy Error",
            description = f"I do not have a role high enough to kick {member.mention} / {member}. Give me a higher role and try again.",
            colour = disnake.Colour.random()
            )
        kickSelfEmbed = disnake.Embed(
            title = "Failed to Kick: That's You!",
            description = "You can't kick yourself. Choose a different member and try again.",
            colour = disnake.Colour.random()
            )
        selfKickEmbed = disnake.Embed(
            title = "Failed to Kick: That's Me!",
            description = "You tried to kick me, that's bad. I can't kick myself... so kick me with another bot, do it yourself, or choose a different member to kick.",
            colour = disnake.Colour.random()
            )

        if not inter.guild.me.guild_permissions.kick_members:
            return await inter.response.send_message(embed = selfPermsEmbed)

        if not inter.author.guild_permissions.kick_members:
            return await inter.response.send_message(embed = permsEmbed)

        if member == inter.guild.me:
            return await inter.response.send_message(embed = selfKickEmbed)
        
        if member == inter.author:
            return await inter.response.send_message(embed = kickSelfEmbed)

        if member.top_role >= inter.author.top_role:
            return await inter.response.send_message(embed = hierEmbed)

        if member.top_role >= inter.guild.me.top_role:
            return await inter.response.send_message(embed = selfHierEmbed)

        await member.kick_members(member, reason=f": {reason}")
        await inter.response.send_message(embed = kickEmbed)


def setup(bot):
    bot.add_cog(Kick(bot))
    print("Loaded Kicking.")