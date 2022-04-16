import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot Setup
PREFIX = ">"
BOT_NAME = "The Feds"
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# Discord Guild ID
GUILD_ID = os.getenv("GUILD_ID")

# Discord Channel IDs

# Discord Role IDs
SCRIPT_KIDDIE_ROLE_ID = os.getenv("SCRIPT_KIDDIE_ROLE_ID")
OVERLORD_ROLE_ID = os.getenv("OVERLORD_ROLE_ID")
PYTHON_ROLE_ID = os.getenv("PYTHON_ROLE_ID")
PYTHON_HELP_ROLE_ID = os.getenv("PYTHON_HELP_ROLE_ID")
UNASSIGNED_ROLE_ID = os.getenv("UNASSIGNED_ROLE_ID")


# Discord Message IDs