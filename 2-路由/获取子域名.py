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

app.config["SERVER_NAME"] = "test.com:5000"


@app.route("/", subdomain="admin")
def static_domain():
    return "static domain"


@app.route("/dynamic", subdomain="<subdomain>")
def dynamic_subdomain(subdomain):
    return subdomain + " .domain"


def main():
    app.run()


if __name__ == '__main__':
    main()
