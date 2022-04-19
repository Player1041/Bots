import disnake
from disnake.ext import commands

class Ban(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ban(self, inter, member: disnake.Member, delete: commands.Range[0,7], reason: str = None):
        """
        Bans a member.
        
        Parameters
        ----------
        
        member: The member you want to ban.
        delete: How many days worth of messages to delete (goes back 7 days at most); 0 for no deleting.
        reason: Shows in audit logs (optional).
        """
        
        banEmbed = disnake.Embed(
            title = "Banned Successfully",
            description = f"{inter.author.mention} / {inter.author} has successfully banned {member} from the server.",
            colour = disnake.Colour.random()
            )
        permsEmbed = disnake.Embed(
            title = "Failed to Ban: Missing Permissions",
            description = f"You ({inter.author.mention} / {inter.author}) do not have the `Ban Members` permission. Get the `Bam Members` permission and try again.",
            colour = disnake.Colour.random()
            )
        selfPermsEmbed = disnake.Embed(
            title = "Failed to Ban: Missing Permissions",
            description = f"I do not have the `Ban Members` permission. Give me the `Ban Members` permission and try again.",
            colour = disnake.Colour.random()
            )
        hierEmbed = disnake.Embed(
            title = "Failed to ban: Hierarchy Error",
            description = f"You ({inter.author.mention} / {inter.author}) do not have a role high enough to ban {member.mention} / {member}. Get a higher role and try again.",
            colour = disnake.Colour.random()
            )
        selfHierEmbed = disnake.Embed(
            title = "Failed to ban: Hierarchy Error",
            description = f"I do not have a role high enough to ban {member.mention} / {member}. Give me a higher role and try again.",
            colour = disnake.Colour.random()
            )
        banSelfEmbed = disnake.Embed(
            title = "Failed to ban: That's You!",
            description = "You can't ban yourself. Choose a different member and try again.",
            colour = disnake.Colour.random()
            )
        selfBanEmbed = disnake.Embed(
            title = "Failed to ban: That's Me!",
            description = "You tried to ban me, that's bad. I can't ban myself... so ban me with another bot, do it yourself, or choose a different member to ban.",
            colour = disnake.Colour.random()
            )

        if not inter.guild.me.guild_permissions.ban_members:
            return await inter.response.send_message(embed = selfPermsEmbed)

        if not inter.author.guild_permissions.ban_members:
            return await inter.response.send_message(embed = permsEmbed)

        if member == inter.guild.me:
            return await inter.response.send_message(embed = selfBanEmbed)
        
        if member == inter.author:
            return await inter.response.send_message(embed = banSelfEmbed)

        if member.top_role >= inter.author.top_role:
            return await inter.response.send_message(embed = hierEmbed)

        if member.top_role >= inter.guild.me.top_role:
            return await inter.response.send_message(embed = selfHierEmbed)

        await inter.guild.ban(member, delete_message_days = delete, reason=f": {reason}")
        await inter.response.send_message(embed = banEmbed)


def setup(bot):
    bot.add_cog(Ban(bot))
    print("Loaded Ban Management")