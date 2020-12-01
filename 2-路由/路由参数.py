# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 第一种路由.py
@time: 2020/12/1 10:02
@desc:
"""

from flask import Flask

app = Flask(__name__)


# 通过装饰器 添加路由
# @app.route('/test/<int:id>')
# @app.route('/test/<float:id>')
# @app.route('/test/<path:id>')
@app.route('/test/<uuid:id>')
def index(id):
    print(id)
    print(type(id))
    return {
        'code': 1,
        'msg': 'hello flask'
    }


def main():
    app.run()


if __name__ == '__main__':
    main()
