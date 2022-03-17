from jinja2 import Template


def index():
    with open('templates/index.html', 'r') as f:
        data = f.read()

    tem = Template(data)
    response = tem.render(info={'webserver': 'mfserver', 'other_server': ['django', 'flask']})
    return response.encode('utf-8')


def error():
    return '<h1>404 NOT FOUND<h1>'.encode('utf-8')
