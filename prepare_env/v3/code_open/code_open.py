import json
import os
import subprocess
import sys

from helper.helper import check_project_name, get_settings

SETTING_KEY = 'work_paths'

def code_open(paths):
    status_code = 0
    for path in paths:
        status_code += subprocess.check_call("code {0}".format(path), shell=True)
    if status_code > 0:
        # 決めつけている もしかしたらシステムエラーかも
        print("[!] dev_info.jsonへworkdirの記述がないか\n記述が間違っています")
        sys.exit(1)

data = None
project_name = None
if __name__ == '__main__':
    project_name = check_project_name(sys.argv)
    paths = get_settings(project_name, SETTING_KEY)
    code_open(paths)
