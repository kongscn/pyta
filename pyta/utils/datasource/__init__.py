__author__ = 'kongs'

from abc import ABCMeta, abstractmethod

class DataSource(meta=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_hist_code(self):
        pass
