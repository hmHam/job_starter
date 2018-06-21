#!/bin/bash
#!/usr/bin
#!/home/user/.pyenv/shims/
#!/home/user/.nodebrew/current/bin/
tab_name=(
  'ng-build'
  'frontend'
  'runserver'
  'backend'
  'shell'
)
path=(
  'workspace/cs-report_frontend/csReport'
  'workspace/cs-report_frontend/csReport'
  'workspace/cs_report_backend/src'
  'workspace/cs_report_backend/src'
  'workspace/cs_report_backend/src'
)
ng_build_index=0
runserver_index=2
shell_index=4

for g in 0 1 2 3 4
do
  guake -n ${path[$g]}
  guake --rename-current-tab=${tab_name[$g]}
  if [ $g = 0 ]; then
      guake -e "ng build --watch"
	elif [ $g = 1 -o $g = 3 ]; then
			guake -e "git branch"
  elif [ $g = 2 ]; then
      guake -e "python manage.py runserver"
	elif [ $g = 4 ]; then
      guake -e "python manage.py shell"
  fi
done
