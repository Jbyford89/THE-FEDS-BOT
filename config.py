import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot Setup
PREFIX = ">"
BOT_NAME = "The Feds"
BOT_TOKEN = os.environ["DISCORD_TOKEN"]
OWNER_ID = os.environ["OWNER_ID"]

# Discord Guild ID
GUILD_ID = os.environ["GUILD_ID"]

# Discord Channel IDs

# Discord Role IDs
SCRIPT_KIDDIE_ROLE_ID = os.environ["SCRIPT_KIDDIE_ROLE_ID"]
OVERLORD_ROLE_ID = os.environ["OVERLORD_ROLE_ID"]
PYTHON_ROLE_ID = os.environ["PYTHON_ROLE_ID"]
PYTHON_HELP_ROLE_ID = os.environ["PYTHON_HELP_ROLE_ID"]
UNASSIGNED_ROLE_ID = os.environ["UNASSIGNED_ROLE_ID"]


# Discord Message IDs
