# -*- coding: utf-8 -*-
'''

'''

__author__ = 'kongs'
# TODO: add method to store result.

import os.path as path
import logging

from numpy.core.records import fromrecords
import pandas as pd
from pandas.io.data import DataReader, get_components_yahoo

import utils.log
from utils.config import CONFIG
from strategies.macd import MACD
from utils.common import rec2csv



logger = logging.getLogger(__name__)

def opt(products):
    from datetime import datetime as dt
    print('Start at %s' % dt.now())
    recs=[]
    calculations=0
    model = MACD()

    for product in products:
        model.product=product
        cals, rec = opt_single(model)
        recs += rec
        calculations += cals

    recs = fromrecords(recs, names=['code', 'revenue', 'nfast', 'nslow', 'nmacd'])
    rec2csv(recs, path.join(CONFIG['out_p'],'opt.csv'), mode='a', with_header=True)

    print('End at %s' % dt.now())
    print('Total %s macd combinations computed.' % calculations)


def opt_single(model):
    # if len(p) < 200:
    #     logger.warning('CODE %s has only %d records, not enough.', p.code, len(p))
    #     return
    cals = 0

    recs = []

    for nfast in range(6, 24):
        #logger.info('Start CODE=%s, nfast=%d', model.products[0].code, nfast)
        for nslow in range(nfast+5, 31):
            for nmacd in range(6, 15):
                cals += 1
                model.nfast=nfast
                model.nslow=nslow
                model.nmacd=nmacd
                model.analyze()
                recs.append((model.product.code, model.revenue, nfast, nslow, nmacd))

    return cals, recs


def main():
    period = 'd'
    date_from = '2003-01-01'
    date_to = '2013-01-01'

#    db = psql.get_db()
#    product_codes = db.prepare('''SELECT p.code AS code, p.id as id
#        FROM products p LEFT JOIN companies c ON p.company_id = c.id
#        WHERE c.sector IS NOT NULL
#        and p.id < 9354
#        ORDER BY p.id''')()

    product_codes = get_components_yahoo('^DJI').index
    cur = 0
    all = len(product_codes)
    logger.info('Start main loop consist of %d products.', len(product_codes))

    for code in product_codes:
        cur += 1
        logger.info('(%d/%d) %s started.',cur, all, code)


        product = DataReader(code, 'yahoo', start=date_from, end=date_to)

        product.code = code

        opt(product)

def demo():
    code='AAPL'
    date_from = '2003-01-01'
    date_to = '2013-01-01'
    product = DataReader(code, 'yahoo', start=date_from, end=date_to)
    product.code = code
    opt([product])

def democsv():
    from utils.config import CONFIG
    from os.path import join
    histf=join(CONFIG['temp_p'], 'AAPL.csv')
    product = pd.read_csv(histf, index_col=0)
    product.code='aapl'
    opt([product])


if __name__ == '__main__':
    # main()

    from timeit import Timer
    t = Timer("demo()", "from __main__ import demo")
    print(t.repeat(repeat=1, number=1))
