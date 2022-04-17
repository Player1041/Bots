import disnake
from disnake.ext import commands
import os


class Kick(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def kick(self, inter, member: disnake.Member, reason: str = None):
        kickEmbed = disnake.Embed(
            title = "Kicked Successfully",
            description = f"{inter.author.mention} / {inter.author} has successfully kicked {member} from the server."
            )
        permsEmbed = disnake.Embed(
            title = "Failed to Kick: Missing Permissions",
            description = f"You ({inter.author.mention} / {inter.author}) do not have the `Kick Members` permission. Get the `Kick Members` permission and try again."
            )
        selfPermsEmbed = disnake.Embed(
            title = "Failed to Kick: Missing Permissions",
            description = f"I do not have the `Kick Members` permission. Give me the `Kick Members` permission and try again."
            )
        hierEmbed = disnake.Embed(
            title = "Failed to kick: Hierarchy Error",
            description = f"You ({inter.author.mention} / {inter.author}) do not have a role high enough to kick {member.mention} / {member}. Get a higher role and try again."
            )
        selfHierEmbed = disnake.Embed(
            title = "Failed to kick: Hierarchy Error",
            description = f"I do not have a role high enough to kick {member.mention} / {member}. Give me a higher role and try again."
            )
        
        if not inter.guild.me.guild_permissions.kick_members:
            return await inter.response.send_message(embed = selfPermsEmbed)
        if 