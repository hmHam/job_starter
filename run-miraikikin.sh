tab_name=('ng-build' 'frontend' 'runserver' 'backend')
path=('workspace/miraikikin_frontend/miraikikin' 'workspace/miraikikin_frontend/miraikikin' 'workspace/bm_miraikikin/src' 'workspace/bm_miraikikin/src')

for g in 0 1 2 3 4 5
do
  /usr/bin/guake -n ${path[$g]}
  /usr/bin/guake --rename-current-tab=${tab_name[$g]}
done
Add Comment Collapse



