# coding:utf-8

from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter  # 导入

app = Flask(__name__)


# 1. 自定义转换器 (继承BaseConverter)
class RegexConverter(BaseConverter):

    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    # 重写父类的to_python()方法。 (可以对url参数做预处理，类型转换等)
    def to_python(self, value):
        print('to_python()被调用了')
        # value参数就是url中匹配出的内容。
        # 可以在to_python()方法中对url参数做预处理、类型转换等 (转换器本质)
        return value  # return的返回值就是传递给视图函数的值

    # 重写父类的to_url()方法。 使用url_for方法的时候被调用(url反向解析)
    def to_url(self, value):
        print('to_url()被调用了')
        # value就是url_for()中传递的参数。
        # return "15811111111"
        return value  # 返回值就是url路由正则匹配出的url部分。


# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter


# 127.0.0.1:5000/send/18612345678
@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
def send_sms(mobile_num):
    return f"send sms to {mobile_num}"


@app.route("/index")
def index():
    # url反向解析，根据send_sms视图获取对应的url。 (会调用转换器的to_url()方法)
    url = url_for("send_sms", mobile_num="18912341235")  # mobile_num对应视图函数接收的形参。
    # url = "/send/18912341235"
    return redirect(url)


if __name__ == '__main__':
    app.run()
