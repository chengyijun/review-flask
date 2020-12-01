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


def index():
    return {
        'code': 1,
        'msg': 'hello flask'
    }


# 通过add_url_rule() 方式添加路由  其实上第一种装饰器方式 也是内部调用了该方法实现
app.add_url_rule('/', None, index)


def main():
    app.run()


if __name__ == '__main__':
    main()
