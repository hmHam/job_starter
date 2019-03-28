import json
import os
import subprocess
import sys

from helper.func import check_project_name, get_settings

SETTING_KEY = 'workdir'

def set_environment(workdirs):
    for workdir in workdirs:
        tab_name = workdir[0]
        path = workdir[1]
        commands = workdir[2] if isinstance(workdir[2], list) else [workdir[2]]
        status_code = 0
        subprocess.call('guake --new-tab={path}'.format(path=path), shell=True)
        i = subprocess.getoutput('guake -g')
        subprocess.call(
            "guake -i {i} --rename-tab='{tab_name}'".format(
                i=i, tab_name=tab_name), shell=True)
        for command in commands:
            status_code += subprocess.check_call(
            "guake -i {i} --execute-command='{command}'".format(
                i=i, command=command), shell=True)
        if status_code > 0:
            # 決めつけている もしかしたらシステムエラーかも
            print("dev_info.jsonへworkdirの記述がないか\n記述が間違っています")
            sys.exit(1)
    subprocess.call('exit')

data = None
project_name = None
if __name__ == '__main__':
    project_name = check_project_name(sys.argv)
    workdirs = get_settings(project_name, SETTING_KEY)
    set_environment(workdirs)

