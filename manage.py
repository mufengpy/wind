from wsgiref.simple_server import make_server
import settings


def index():
    return '<h1>Welcome to mfserver<h1>'.encode('utf-8')


def error():
    return '<h1>404 NOT FOUND<h1>'.encode('utf-8')


urls = [
    ('/', index),
]


# 函数对http请求与响应的封装、使得Python专注与HTML
# environ http 请求 (dist)
# start_response 响应 (function)
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
        response = error()

    return [response]


if __name__ == '__main__':
    httpd = make_server('', settings.port, app)
    print(settings.info_terminal)
    httpd.serve_forever()
