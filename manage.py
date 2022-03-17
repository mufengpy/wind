# coding:utf-8
__author__ = 'mfserver'

from wsgiref.simple_server import make_server
from whitenoise import WhiteNoise

import settings
from app01.urls import urls
from app01 import views


# 函数对http请求与响应的封装、使得Python专注与HTML
# env http 请求 (dist)
# response 响应 (function)
def app(env, response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    response(status, headers)

    path = env['PATH_INFO']  # 拿到请求体中的路由
    func = None
    for url in urls:
        if url[0] == path:
            func = url[1]
            break

    if func:
        response = func()
    else:
        response = views.error()

    return [response]


if __name__ == '__main__':
    whitenoise = WhiteNoise(app, root='static')
    httpd = make_server('', settings.port, whitenoise)
    print(settings.info_terminal)
    httpd.serve_forever()
