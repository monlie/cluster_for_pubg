# -*- coding: utf-8 -*-
"""
Created on 2017/9/24 23:23:46

@author: 李蒙
"""

from time import time


def run_time(func):
    def wapper(*args, **kwargs):
        start = time()
        back = func(*args, **kwargs)
        end = time()
        print('function %s runs %.3fs' % (func.__name__, end-start))
        return back
    return wapper