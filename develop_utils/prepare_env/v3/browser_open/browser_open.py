import json
import os
import subprocess
import sys

from helper.func import check_project_name, get_settings

BROWSER_NAME = 'google-chrome'
SETTING_KEY = 'urls'

def browser_open(paths):
    status_code = 0
    for path in paths:
        status_code += subprocess.check_call("{0} {1}".format(BROWSER_NAME, path), shell=True)
    if status_code > 0:
        # 決めつけている もしかしたらシステムエラーかも
        print("設定ファイルにurlsの記述がないか\n記述が間違っています")
        sys.exit(1)

data = None
project_name = None
if __name__ == '__main__':
    project_name = check_project_name(sys.argv)
    urls = get_settings(project_name, SETTING_KEY)
    browser_open(urls)
