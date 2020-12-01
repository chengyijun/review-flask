# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 中间件.py
@time: 2020/12/1 18:10
@desc:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'index1111'


class Middleware:
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        print('do something...')
        return self.old_wsgi_app(environ, start_response)


def my_middle(old_wsgi_app):
    def inner(environ, start_response):
        print('做点事情...')
        return old_wsgi_app(environ, start_response)

    return inner


def main():
    # app.wsgi_app = Middleware(app.wsgi_app)
    app.wsgi_app = my_middle(app.wsgi_app)
    app.run()


if __name__ == '__main__':
    main()
