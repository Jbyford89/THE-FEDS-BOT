import nextcord
from nextcord.ext import commands
from nextcord.embeds import EmptyEmbed
import config

class MyHelpCommand(commands.MinimalHelpCommand):
    """Custom help command override using embeds."""

    COLOUR = nextcord.Colour.red()

    def get_ending_note(self):
        """Returns note to place at the end of the help command."""
        invoked_with = self.invoked_with
        return f'Use {config.PREFIX}{invoked_with} [command] for more info on a command.'

    def get_command_signature(self, command):
        """Returns the signature portion of the help command."""
        return f"{command.qualified_name} {command.signature}"

    async def send_bot_help(self, mapping: dict):
        """"Implements bot command help page"""
        embed = nextcord.Embed(title="Bot Commands", colour=self.COLOUR)
        avatar = self.context.bot.user.avatar
        avatar_url = avatar.url if avatar else EmptyEmbed
        embed.set_author(name=self.context.bot.user.name, icon_url=avatar_url)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            name = "No Category" if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                # \u2002 = middle dot
                value = "\u2002".join(f"{config.PREFIX}{c.name} {c.signature}" for c in filtered)
                if cog and cog.description:
                    value = f"{cog.description}\n\n{value}"
                embed.add_field(name=name, value=value, inline=False)


        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog: commands.Cog):
        """"Implements cog command help page"""
        embed = nextcord.Embed(f"{cog.qualified_name} Commands", colour=self.COLOUR)
        if cog.description:
            embed.description = cog.description

            filtered = await self.filter_commands(cog.get_commands(), sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command), 
                    value=command.short_doc or "No help given", inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group: commands.Group):
        """Implements group help page and command help page"""
        embed = nextcord.Embed(title = f"{group.qualified_name} Commands", colour=self.COLOUR)
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command),
                    value=command.short_doc or "No help given", inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
    
    # Use the same function as group help for command help
    send_command_help = send_group_help
