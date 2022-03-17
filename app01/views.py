# def index():
#     return '<h1>Welcome to mfserver<h1>'.encode('utf-8')


def index():
    with open('templates/index.html', 'rb') as f:
        data = f.read()
    return data


def error():
    return '<h1>404 NOT FOUND<h1>'.encode('utf-8')
