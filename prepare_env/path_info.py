BACKEND_PATH = 'workspace/' + project_name + '_backend/src'
FRONTEND_PATH = 'workspace/' + project_name + '_frontend/' + project_name

VS_CODE_WORKDIR_LIST = [BACKEND_PATH, FRONTEND_PATH]

GUAKE_WORKDIR_LIST = [
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

CHROME_WORKDIR_LIST = [
]