__author__ = 'kongs'

from pandas.io.data import DataReader

from util.datasource import DataSource

class OnlineDS(DataSource):
    def __init__(self, provider='yahoo',
                 startdt='19900101'):
        self.provider=provider

    def get_hist_code(self, code):
        return DataReader(code, self.provider, )

