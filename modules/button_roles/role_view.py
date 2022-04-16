from async_timeout import timeout
import nextcord
import config

from utils.utils import custom_id

VIEW_NAME = "RoleView"

class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        # If user has role
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Your {role.name} role has been removed.", ephemeral=True)
        # If user doesn't have role
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been given the role {role.name}.", ephemeral=True)


    @nextcord.ui.button(label="Script Kiddie", emoji="🤖", style=nextcord.ButtonStyle.primary, custom_id=custom_id(VIEW_NAME, config.SCRIPT_KIDDIE_ROLE_ID))
    async def script_kiddie_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @nextcord.ui.button(label="Python", emoji="🐍", style=nextcord.ButtonStyle.blurple, custom_id=custom_id(VIEW_NAME, config.PYTHON_ROLE_ID))
    async def python_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @nextcord.ui.button(label="Python Help", emoji="🆘", style=nextcord.ButtonStyle.blurple, custom_id=custom_id(VIEW_NAME, config.PYTHON_HELP_ROLE_ID))
    async def python_help_button(self, button, interaction):
        await self.handle_click(button, interaction)

    
