import logging

from pyrogram import Client

from tgpy.context import Context
from tgpy.version import __version__  # noqa: F401

logging.basicConfig(
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)
logging.getLogger('pyrogram').setLevel(logging.WARNING)


class App:
    client: Client
    ctx: Context

    def __init__(self):
        self.ctx = Context()


app = App()

__all__ = ['App', 'app']
