# -*- coding: utf-8 -*-
def abs(n):
    '''
    :type n: int
    :param n: 这是一个数字，返回绝对值
    :return: 参数的绝对值
    '''
    if n < 0:
        return -n
    return n

help(abs)