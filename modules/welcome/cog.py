import nextcord
from nextcord.ext import commands
import config

class WelcomeCog(commands.Cog, name="welcome"):
    """Welcome new users to the server."""

    def __init__(self, bot: commands.bot):
        self.bot = bot        

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        """Sends a welcome message to the server when someone joins."""
        guild =self.bot.get_guild(config.GUILD_ID)
        intro_channel = guild.get_channel(config.WELCOME_CHANNEL_ID)
        rules_channel = guild.get_channel(config.RULES_CHANNEL_ID)
        role_channel = guild.get_channel(config.ROLE_ASSIGNMENT_ID)
        # Do not welcome bots or members of other guilds the bot is in.
        if member.bot or member.guild != guild:
            return
        # Send a welcome message to the server.
        await intro_channel.send(
            f"Welcome to {guild.name} {member.mention}!\n"
            f"Please read the rules in {rules_channel.mention} and have fun!\n"
            f"Make sure to check out the {role_channel.mention} channel for role assignments!"
        )
        # Give the unassigned role to the new member.
        await member.add_roles(guild.get_role(config.UNASSIGNED_ROLE_ID))