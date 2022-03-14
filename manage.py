from wsgiref.simple_server import make_server


# 函数对http请求与响应的封装、使得Python专注与HTML
# environ http 请求 (dist)
# start_response 响应 (function)
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return [b'<h1>Hello, web!</h1>']


if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    print('''
mfserver version 1.0, using settings 'mfserver.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
    ''')
    httpd.serve_forever()