import os
import subprocess
import sys

args = sys.argv

try:
    project_name = args[1]
    print(project_name)
except IndexError:
    raise Exception('プロジェクト名を選んでください')
    exit()

BACKEND_PATH = 'workspace/' + project_name + '_backend/src'
FRONTEND_PATH = 'workspace/' + project_name + '_frontend/' + project_name

path_list = [BACKEND_PATH, FRONTEND_PATH]
for i in path_list:
    os.system("code -n -a {0}".format(i))

path_info = [
    {
     'path': FRONTEND_PATH,
     'tab_name': 'start:proxy',
     'command': 'npm run start:proxy'
    },
    {
     'path': FRONTEND_PATH,
     'tab_name': 'frontend',
     'command': 'git branch'
    },
    {
     'path': BACKEND_PATH,
     'tab_name': 'runserver',
     'command': 'python manage.py runserver'
    },
    {
     'path': BACKEND_PATH,
     'tab_name': 'backend',
     'command': 'git branch'
    },
    {
     'path': BACKEND_PATH,
     'tab_name': 'shell',
     'command': 'python manage.py shell'
    },
]

for item in path_info:
    os.system(
        "guake --new-tab={path}".format(path=item['path']))
    i = subprocess.getoutput("guake -g")
    os.system(
        "guake -i {index} --rename-tab='{tab_name}'".format(
            index=i, tab_name=item['tab_name']))
    os.system(
        "guake -i {index} --execute-command='{command}'".format(
            index=i, command=item['command']))
