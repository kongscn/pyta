# -*- coding: utf-8 -*-
__author__ = 'kongs'

import os
import os.path as path

CONFIG = dict()

proj_p = path.dirname(path.dirname(path.realpath(__file__)))
CONFIG['base_p'] = proj_p
CONFIG['log_p'] = path.join(proj_p, 'log')
CONFIG['out_p'] = path.join(proj_p, 'out')
CONFIG['data_p'] = path.join(proj_p, 'data')
CONFIG['temp_p'] = path.join(proj_p, 'temp')

for key in CONFIG.keys():
    os.makedirs(CONFIG[key], exist_ok=True)
