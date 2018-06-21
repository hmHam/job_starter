import os
import subprocess
import sys

args = sys.argv

try:
    project_name = args[1]
except IndexError:
    raise Exception('プロジェクト名を選んでください')
    exit()

path_info = [
    {
     'path': 'workspace/' + project_name + '_frontend/' + project_name,
     'tab_name': 'ng build',
     'command': 'ng build --watch'
    },
    {
     'path': 'workspace/' + project_name + '_frontend/' + project_name,
     'tab_name': 'frontend',
     'command': 'git branch'
    },
    {
     'path': 'workspace/' + project_name + '_backend/src',
     'tab_name': 'runserver',
     'command': 'python manage.py runserver'
    },
    {
     'path': 'workspace/' + project_name + '_backend/src',
     'tab_name': 'backend',
     'command': 'git branch'
    },
    {
     'path': 'workspace/' + project_name + '_backend/src',
     'tab_name': 'shell',
     'command': 'python manage.py shell'
    },
]

for item in path_info:
    os.system("guake --new-tab={path}".format(path=item['path']))
    i = subprocess.getoutput("guake -g")
    os.system(
        "guake -i {index} --rename-tab='{tab_name}'".format(
            index=i, tab_name=item['tab_name'])
        )
    os.system(
        "guake -i {index} --execute-command='{command}'".format(
            index=i, command=item['command'])
        )
