import json
import os
import subprocess
import sys

from helper.func import check_project_name
from browser_open import browser_open
from code_open import code_open
from set_environment import set_environment

project_name = check_project_name(sys.argv)

with open(os.path.join(os.path.dirname(__file__), 'dev_info.json'), 'r') as f:
    try:
        data = json.load(f)[project_name]
        urls = data['urls']
        paths = data['work_paths']
        workdirs = data['workdir']
    except KeyError:
        print("設定ファイルにプロジェクト用の記述がありません")
        sys.exit(1)

    browser_open(urls)
    code_open(paths)
    set_environment(workdirs)
