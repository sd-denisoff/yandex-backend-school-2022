import logging
import os
import sys

from django.conf import settings

logs_path = settings.BASE_DIR / 'logs'


def configure_logger(name, level=logging.DEBUG, dest='file'):
    LOGGER = logging.getLogger(name)
    LOGGER.setLevel(level)

    if dest == 'file':
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)
        os.chmod(logs_path, 0o777)
        handler = logging.FileHandler(f'logs/{name}.log')
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)

    return LOGGER
