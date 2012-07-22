from ..settings import *

#Small check to make sure we're on DotCloud. 
#Interesting snippet. Keep in for the moment, will write a test for it in the future. 
import getpass
if getpass.getuser() == 'dotcloud': 
    DOTCLOUD = True 

import json
if DOTCLOUD:
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',    
            'NAME': 'template1', #Change this. 
            'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
            'HOST': env['DOTCLOUD_DB_SQL_HOST'],
            'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
    }
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# settings/local.py is ignored to allow for easy settings
# overrides without affecting others
try:
    from local import *
except ImportError:
    pass
