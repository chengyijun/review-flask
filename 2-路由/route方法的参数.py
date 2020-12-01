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
@app.route('/old', methods=['GET', 'POST'], endpoint='x1', redirect_to='/new')
def old_fuc():
    return {
        'code': 1,
        'msg': 'hello flask'
    }


@app.route('/new')
def new_fuc():
    return 'new'


def main():
    app.run()


if __name__ == '__main__':
    main()
