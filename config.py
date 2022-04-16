import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot Setup
PREFIX = ">"
BOT_NAME = "The Feds"
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# Discord Guild ID
GUILD_ID = int(os.getenv("GUILD_ID"))

# Discord Channel IDs

# Discord Role IDs
SCRIPT_KIDDIE_ROLE_ID = int(os.getenv("SCRIPT_KIDDIE_ROLE_ID"))
OVERLORD_ROLE_ID = int(os.getenv("OVERLORD_ROLE_ID"))
PYTHON_ROLE_ID = int(os.getenv("PYTHON_ROLE_ID"))
PYTHON_HELP_ROLE_ID = int(os.getenv("PYTHON_HELP_ROLE_ID"))
UNASSIGNED_ROLE_ID = int(os.getenv("UNASSIGNED_ROLE_ID"))


# Discord Message IDs