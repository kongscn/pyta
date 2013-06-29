# -*- coding: utf-8 -*-
__author__ = 'kongs'

import logging
import os.path as path
from utils.config import CONFIG

logger = logging.getLogger('')
logger.setLevel(logging.INFO)

fh = logging.FileHandler(path.join(CONFIG['log_p'], 'app.log'))
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

fmt = '%(asctime)s %(levelname)-7s %(name)s %(message)s'
dtfmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt, dtfmt)

fmt='%(asctime)s %(levelname)-7s %(message)s'
dtfmt =  '%H:%M:%S'
formatter_simple = logging.Formatter(fmt, dtfmt)

fh.setFormatter(formatter)
ch.setFormatter(formatter_simple)

logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logger=logging.getLogger(__name__)
    logger.info('huha')

