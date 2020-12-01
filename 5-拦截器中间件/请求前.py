# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 请求.py
@time: 2020/12/1 16:27
@desc:
"""

from flask import Flask

app = Flask(__name__)


@app.before_request
def before1():
    print('before1')


@app.before_request
def before2():
    print('before2')


@app.after_request
def after1(respose):
    print('after1')
    return respose


@app.after_request
def after2(respose):
    print('after2')
    return respose


"""
拦截器执行结果：
before1
before2
after2
after1
before是顺序执行的
after 是倒序执行的
"""


@app.route('/index')
def index():
    return 'index'


def main():
    app.run()


if __name__ == '__main__':
    main()
