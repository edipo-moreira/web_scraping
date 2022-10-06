from enum import Enum
import logging
from rich.logging import RichHandler
import os

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[
        RichHandler(
            level=logging.INFO if os.getenv("debug") == "false" else logging.DEBUG
        )
    ],
)


class Config(Enum):
    ATTEMPTS = 3
    RETRY_TIME = 60
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
    LOGGER = logging.getLogger("rich")
