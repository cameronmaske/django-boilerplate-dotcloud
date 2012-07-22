#!/usr/bin/env python
import os, sys
import getpass

if __name__ == '__main__':
    if getpass.getuser() == 'dotcloud': 
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.environments.production') 
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.environments.development')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
