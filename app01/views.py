from jinja2 import Template
from .models import User, engine, sessionmaker


def index():
    with open('templates/index.html', 'r') as f:
        data = f.read()

    tem = Template(data)
    response = tem.render(info={'webserver': 'mfserver', 'other_server': ['django', 'flask']})
    return response.encode('utf-8')

def index():
    with open('templates/index.html', 'r') as f:
        data = f.read()

    tem = Template(data)
    response = tem.render(info={'webserver': 'mfserver', 'other_server': ['django', 'flask']})
    return response.encode('utf-8')

def objs_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []

    for obj in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(obj.__dict__)
        obj_arr.append(dict)

    return obj_arr


def user():
    with open('templates/user.html', 'r') as f:
        data = f.read()

    tem = Template(data)

    Session = sessionmaker(bind=engine)
    session = Session()

    user_list = session.query(User).all()
    user_list = objs_to_dicts(user_list)

    session.commit()
    session.close()

    print(user_list)
    response = tem.render(users=user_list)

    return response.encode('utf-8')


# def error():
#     return '<h1>404 NOT FOUND<h1>'.encode('utf-8')
