# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 配置.py
@time: 2020/12/1 9:20
@desc:
"""
from flask import Flask

app = Flask(__name__)
# 通过反射 读取配置文件类
app.config.from_object('settings.TestConfig')


@app.route('/')
def index():
    return {
        'code': 1,
        'msg': 'hello flask'
    }


def main():
    app.run()


if __name__ == '__main__':
    main()
