# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: main.py
@time: 2020/12/1 10:10
@desc:
"""


def main():
    obj = __import__('0-test')
    print(obj.ProductConfig)
    print(obj.ProductConfig.DEBUG)


if __name__ == '__main__':
    main()
