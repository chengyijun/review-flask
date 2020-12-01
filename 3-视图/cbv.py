# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: cbv.py
@time: 2020/12/1 16:11
@desc:
"""

from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


def decorator(fun):
    def inner(*args, **kwargs):
        print('装饰器被执行了')
        return fun(*args, **kwargs)

    return inner


class Login(MethodView):
    methods = ['GET', 'POST']
    decorators = [decorator]

    def get(self):
        return 'hi cbv'

    def post(self):
        return 'hi cbv post'


app.add_url_rule('/login', view_func=Login.as_view(name='login'))


def main():
    app.run()


if __name__ == '__main__':
    main()
