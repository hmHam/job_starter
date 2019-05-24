import sys
import os

try:
    project = sys.argv[1]
except IndexError:
    print("browser-open: プロジェクト名を記入してください")
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'urls', project + '.txt')) as f:
    urls = f.read().split('\n')
    print(urls)
    for url in urls:
        os.system(
            "google-chrome {url}".format(url=url))