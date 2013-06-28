
'''
Test the moving average algo


'''

import pandas as pd

from strategies.macd import MACD



__author__ = 'kongs'


if __name__ == '__main__':
    ts=list(range(100)) + list(range(100,0,-1))
    ts=ts*2

    index=pd.date_range('2001-01-01', periods=len(ts))

    ts=pd.Series(ts, index=index)
    ts.name='Close'

    product=pd.DataFrame(ts)
    product.code='TProduct'

    macd=MACD()
    macd.product=product

    macd.analyze()
    macd.summary()