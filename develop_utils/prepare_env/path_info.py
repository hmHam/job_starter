import os

class PATH_INFO:
    def __init__(self, project_name):
        HOME_DIR = os.path.expanduser('~')
        self.BACKEND_PATH = '{home}/workspace/{pj_name}_backend'.format(home=HOME_DIR, pj_name=project_name)
        self.FRONTEND_PATH = '{home}/workspace/{pj_name}_frontend'.format(home=HOME_DIR, pj_name=project_name)
        self.VS_CODE_WORKDIR = [self.BACKEND_PATH, self.FRONTEND_PATH]
        frontend_workdir = self.FRONTEND_PATH + project_name
        backend_workdir = self.BACKEND_PATH + 'src'
        self.GUAKE_WORKDIR = [
            {
            'path': frontend_workdir,
            'tab_name': 'start:proxy',
            'command': 'npm run start:proxy'
            },
            {
            'path': frontend_workdir,
            'tab_name': 'frontend',
            'command': 'git branch'
            },
            {
            'path': backend_workdir,
            'tab_name': 'runserver',
            'command': 'python manage.py runserver'
            },
            {
            'path': backend_workdir,
            'tab_name': 'backend',
            'command': 'git branch'
            },
            {
            'path': backend_workdir,
            'tab_name': 'shell',
            'command': 'python manage.py shell'
            },
        ]
        self.CHROME_WORKDIR = [
            'git.uci-sys.jp/osaka_univ/cs_web/cs-report_frontend',
            'git.uci-sys.jp/osaka_univ/cs_web/cs-report_frontend/issues',
            'git.uci-sys.jp/osaka_univ/cs_web/cs-report_backend',
            'git.uci-sys.jp/osaka_univ/cs_web/cs-report_backend/issues',
        ]
