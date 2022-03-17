from wsgiref.simple_server import make_server
import settings


# 函数对http请求与响应的封装、使得Python专注与HTML
# environ http 请求 (dist)
# start_response 响应 (function)
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return ['<h1>Hello, web!</h1>'.encode('utf-8')]


if __name__ == '__main__':
    httpd = make_server('', settings.port, app)
    print(settings.info_terminal)
    httpd.serve_forever()