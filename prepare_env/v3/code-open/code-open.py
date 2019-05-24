import sys
import os
import json

try:
    project = sys.argv[1]
except IndexError:
    print("code-open: プロジェクト名を記入してください")
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'project-path', project + '.json')) as f:
    path_infos = json.load(f)
    for new_window_group_name, file_paths in path_infos.items():
        os.system(
            "code -n {path}".format(path=file_paths[0]))
        if len(file_paths) > 2:
            for path in file_paths[1:]:
                os.system(
                    "code -a {path}".format(path=path))