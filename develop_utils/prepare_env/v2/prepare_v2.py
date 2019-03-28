import sys
import argparse
import os
import glob
import subprocess

sys.path.append(os.path.join(os.getcwd(), '..'))
import path_info

args = sys.argv

try:
    project_name = args[1]
    path_info_instance = path_info.PATH_INFO(project_name)
except IndexError:
    raise Exception('プロジェクト名を選んでください')
    exit()

## FIXME: vscodeの作業スペースがおかしい
for i, item in enumerate(path_info_instance.VS_CODE_WORKDIR):
    print(item)
    os.system("code {0} --new-window".format(item))

# for item in path_info_instance.GUAKE_WORKDIR:
#     os.system(
#         "guake --new-tab={path}".format(path=item['path']))
#     i = subprocess.getoutput("guake -g")
#     os.system(
#         "guake -i {index} --rename-tab='{tab_name}'".format(
#             index=i, tab_name=item['tab_name']))
#     os.system(
#         "guake -i {index} --execute-command='{command}'".format(
#             index=i, command=item['command']))

# os.system("google-chrome")
# for url in path_info_instance.CHROME_WORKDIR:
#     os.system(
#         "google-chrome {url}".format(url=url)
#     )