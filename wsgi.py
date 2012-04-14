#Note: Change APP_NAME
import os
os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import sys
sys.path.append('/home/dotcloud/current/{{ project_name }}')