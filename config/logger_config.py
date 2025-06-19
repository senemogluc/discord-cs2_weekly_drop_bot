import logging


logging.basicConfig(
    filename='discord.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    encoding='utf-8'
)