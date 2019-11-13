import json
import os
from pathlib import Path
import subprocess
import argparse

# TODO: ブラウザででに開いてるページは開かない
# TODO: シェルですでに開いてる画面は開かない

parser = argparse.ArgumentParser(description='開発用環境をコマンドで開く')
parser.add_argument('project_name', help='開発プロジェクト名を指定')
# エディター指定ができるようにすれば良いかも
parser.add_argument('-c', '--code', action='store_true', help='VSCodeを開くかどうか')
parser.add_argument('-b', '--browser', action='store_true', help='ブラウザを開くかどうか')
parser.add_argument('-s', '--shell', action='store_true', help='シェルを開くかどうか')
parser.add_argument('-i', '--issue-num')
parser.add_argument('-ex', '--exclude', action='store_true')

def browser_open(data, issue_num=None, setting_key='urls', browser_name='google-chrome'):
    paths = data[setting_key]
    status_code = 0
    for path in paths:
        if issue_num is not None and path.endswith('issues/'):
            path += str(issue_num)
        status_code += subprocess.check_call("{0} {1}".format(browser_name, path), shell=True)
    if status_code > 0:
        # 決めつけている もしかしたらシステムエラーかも
        print("設定ファイルにurlsの記述がないか\n記述が間違っています")
        sys.exit(1)


def code_open(data, setting_key='src_paths'):
    paths = data[setting_key]
    status_code = 0
    for path in paths:
        status_code += subprocess.check_call("code {0}".format(path), shell=True)
    if status_code > 0:
        # 決めつけている もしかしたらシステムエラーかも
        print("[!] dev_info.jsonへworkdirの記述がないか\n記述が間違っています")
        sys.exit(1)


def set_environment(data, setting_key='workdirs'):
    workdirs = data[setting_key]
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


if __name__ == '__main__':
    try:
        args = parser.parse_args()
        project_name = args.project_name
    except Exception:
        pass

    SETTING_FILENAME = 'dev_info.json'

    settings = Path.home() / SETTING_FILENAME
    if not settings.exists():
        settings = Path(__file__).parent / SETTING_FILENAME

    with settings.open() as f:
        try:
            data = json.load(f)[project_name]
            if not (args.code or args.browser or args.shell):
                # 何も引数に指定しない場合は全て開く
                browser_open(data, args.issue_num)
                code_open(data)
                set_environment(data)
            if args.exclude:
                # excludeオプションが指定されるとフラグを反転させる
                args.code = not args.code
                args.browser = not args.browser
                args.shell = not args.shell
            if args.code:
                code_open(data)
            if args.browser:
                browser_open(data, args.issue_num)
            if args.shell:
                set_environment(data)
        except KeyError:
            print("設定ファイルにプロジェクト用の記述がありません")
