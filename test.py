import re

path = '/static/css/index.css'
# matchObj = re.match(r'.*(.css)', url)
# print(matchObj.group())
path_list = path.split('/')
path_list = [item for item in path_list if item]
print('/'.join(path_list))
