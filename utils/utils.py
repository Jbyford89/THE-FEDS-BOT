from distutils.command.config import config
import config


def custom_id(view: str, id: int) -> str:
    """Return the view with the id appended to it."""
    return f"{config.BOT_NAME}:{view}:{id}"