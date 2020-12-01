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


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 拿到查询参数
    # print(request.args.to_dict())
    # 拿到post过来的json数据
    # print(json.loads(request.data.decode('utf-8')))
    # 拿到file文件
    # print(request.files.to_dict())
    # file = request.files['file']
    # print(file)
    # file.save('./1.xlsx')
    return 'index'


def main():
    app.run()


if __name__ == '__main__':
    main()
