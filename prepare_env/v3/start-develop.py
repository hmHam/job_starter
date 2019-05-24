import sys
import argparse
import subprocess

def usage():
    return 'usage of this program'

def description():
    return 'description'

def epilog():
    return 'end'

parser = argparse.ArgumentParser(
    prog='start-develop.py',
    usage=usage(),
    description=description(),
    epilog=epilog(),
    add_help=True
)

parser.add_argument('project_name', help='write your develop project name')
parser.add_argument('-c', '--code-open' help='open-your editor', action='store_true')
parser.add_argument('-b', '--browser-open', help='open your browser', action='store_true')
args = parser.parse_args()

try:
    project_name = parser.project_name
except AttributeError:
    print("[!] 開発するプロジェクト名を入力してください")

subprocess.check_call("python3 ./code-open/code-open.py %s" % project_name)
subprocess.check_call("python3 ./browser-open/browser-open.py %s" % project_name)

