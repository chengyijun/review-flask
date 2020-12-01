# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: settings.py
@time: 2020/12/1 9:23
@desc:
"""


class BaseConfig:
    pass


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = False


def main():
    pass


if __name__ == '__main__':
    main()
