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
def check_login():
    print('检查是否登录。。。')


@app.after_request
def add_something(request):
    print('请求之后 做点事')
    return request


@app.route('/index')
def index():
    return 'index'


def main():
    app.run()


if __name__ == '__main__':
    main()
