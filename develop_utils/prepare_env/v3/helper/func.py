import sys
import os
import json
    

def check_project_name(argv):
    try:
        project_name = argv[1]
    except IndexError:
        print("プロジェクト名を入力してください")
        sys.exit(1)
    return project_name

def get_settings(project_name, key):
    with open('../dev_info.json', 'r') as f:
        try:
            paths = json.load(f)[project_name][key]
        except KeyError:
            print("[!] 設定ファイルにエディターのパスを用意するための記述がない\nまたは記述が間違っています")
            paths = []
    