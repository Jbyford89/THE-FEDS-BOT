from nextcord.ext import commands
from .role_view import RoleView
import config

class ButtonRoles(commands.Cog, name="Board Roles"):
    """Creates buttons that assign roles (script-kiddie, Python, etc.) to users.

    Must be used as Admin.

    This command is to bbe used in the designated roles channel. The role buttons will not disappear after being clicked.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(RoleView())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx: commands.Context):
        """Creates a new role view"""
        await ctx.send(f"Click a button to add or remove a role!", view=RoleView())

def setup(bot: commands.Bot):
    bot.add_cog(ButtonRoles(bot))
