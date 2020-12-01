# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 第一种路由.py
@time: 2020/12/1 10:02
@desc:
"""

from flask import Flask, url_for

app = Flask(__name__)


# 通过装饰器 添加路由
@app.route('/')
def index():
    # url_for(endpoint_name) 可以反向生成url
    print(url_for('x1'))
    return {
        'code': 1,
        'msg': 'hello flask',
    }


# endpoint如果不指明 默认为函数名
@app.route('/user', endpoint='x1')
def user():
    return {
        'code': 1,
        'msg': 'hello user'
    }


def main():
    app.run()


if __name__ == '__main__':
    main()
