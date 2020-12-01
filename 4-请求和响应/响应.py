# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 请求.py
@time: 2020/12/1 16:27
@desc:
"""

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    res = make_response({'code': 1})
    res.set_cookie('youname', 'abelrox')
    # res.delete_cookie('youname')
    res.headers['X-something'] = 'hahaha'
    return res


def main():
    app.run()


if __name__ == '__main__':
    main()
