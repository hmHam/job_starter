import sys
import argparse
import os
import glob
import subprocess
from .. import path_info

args = sys.argv

try:
    project_name = args[1]
    print(project_name)
except IndexError:
    raise Exception('プロジェクト名を選んでください')
    exit()

os.system("code --new-window")
for i, item in enumerate(path_info.VS_CODE_WORKDIR_LIST):
    os.system("code --add {0}".format(item))

for item in path_info.GUAKE_WORKDIR_LIST:
    os.system(
        "guake --new-tab={path}".format(path=item['path']))
    i = subprocess.getoutput("guake -g")
    os.system(
        "guake -i {index} --rename-tab='{tab_name}'".format(
            index=i, tab_name=item['tab_name']))
    os.system(
        "guake -i {index} --execute-command='{command}'".format(
            index=i, command=item['command']))

os.system("google-chrome --new-window")
for url in path_info.CHROME_WORKDIR_LIST:
    os.system(
        "google-chrome {url}".format(url=url)
    )