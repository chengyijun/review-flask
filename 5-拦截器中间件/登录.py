# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 请求.py
@time: 2020/12/1 16:27
@desc:
"""

from flask import Flask, session, request, redirect

app = Flask(__name__)
app.secret_key = 'sgsgsgsdgsdgh'


@app.before_request
def check_login():
    print('检查登录')
    if request.path == '/login':
        return None
    if request.path == '/delsession':
        return None
    if request.path == '/setsession':
        return None
    user = session.get('user_info', None)
    print(user)
    if not user:
        return redirect('/login')


@app.route('/login')
def login():
    return '用户登录表单'


@app.route('/setsession')
def set_session():
    session.setdefault('user_info', 'abeltank')
    return '临时设置session'


@app.route('/delsession')
def del_session():
    session.clear()
    return '临时销毁session'


@app.route('/index')
def index():
    return 'index'


def main():
    app.run()


if __name__ == '__main__':
    main()
