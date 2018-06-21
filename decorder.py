import json
import sys
import os

cwd = os.getcwd()


def get_fixture_path():
    for root, dir, files in os.walk(os.path.dirname(cwd)):
        if os.path.basename(root) == 'fixtures':
            return root
    return cwd

read_filepath = os.path.join(get_fixture_path(), sys.argv[1])
try:
    f = open(read_filepath)
except IndexError as ie:
    f.close()
    ie("このコマンドは実行するfixtureファイルのパスが必要です")
json_dict_list = json.load(f)
filename, extension = os.path.filename(read_filepath).split('.')
filename = filename + '_new' + extension
newf = open(os.path.join(os.path.dirname(read_filepath), filename)), 'w')

newf.write('[')
for item in json_dict_list:
    f.write(item)
    f.write('\n')
newf.write(']')
