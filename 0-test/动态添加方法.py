# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 动态添加方法.py
@time: 2020/12/1 18:28
@desc:
"""


class Test:
    def __init__(self, fun):
        self.fun = fun


def hi():
    print('hi')


def main():
    test = Test(hi)
    # setattr(test, 'laugh', hi)

    test.fun()


if __name__ == '__main__':
    main()
