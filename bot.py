version = "the-feds v0.0.1 Beta"
print(f"{version} is loading...")

import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

import config

def main():
    # Allows privledged intents for monitoring members joining/leaving, roles being created/deleted, etc., and role assignments.
    intents = nextcord.Intents.default()
    intents.members = True
    intents.guilds = True

    activity = nextcord.Activity(
        type = nextcord.ActivityType.listening, name=f"{config.PREFIX}help"
    )


    bot = commands.Bot(
        command_prefix=config.PREFIX, 
        description='The Feds Bot',
        activity=activity,
        owner_id=config.OWNER_ID,
        intents=intents)

    

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} is online!")


    # Load cogs
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            bot.load_extension(f"modules.{folder}.cog")

    bot.run(config.BOT_TOKEN)

if __name__ == '__main__':
    main()