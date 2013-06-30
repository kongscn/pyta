# -*- coding: utf-8 -*-
__author__ = 'kongs'

import os

CONFIG = dict()

current_p = os.path.dirname(os.path.realpath(__file__))
proj_p = os.path.dirname(current_p)
CONFIG['base_p'] = proj_p
CONFIG['log_p'] = os.path.join(proj_p, 'log')
CONFIG['out_p'] = os.path.join(proj_p, 'out')
CONFIG['data_p'] = os.path.join(proj_p, 'data')
CONFIG['temp_p'] = os.path.join(proj_p, 'temp')

for key in CONFIG.keys():
    if not os.access(CONFIG[key], os.F_OK):
        os.makedirs(CONFIG[key])
