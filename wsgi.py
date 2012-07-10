"""
WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.environments.development'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import sys
sys.path.append('/home/dotcloud/current/{{ project_name }}')