# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test1.py
@time: 2020/12/1 10:39
@desc:
"""


def main():
    mydict = {
        'code': 1,
        'msg': 'hello flask'
    }
    tmp = mydict.pop('code')
    # tmp = mydict.popitem()
    print(tmp)


if __name__ == '__main__':
    main()
