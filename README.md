Adapted Django Boilerplate (Django 1.4 and DotCloud)
===========================================
A barebones default layout taken from https://github.com/martinogden/django-boilerplate (see credits).

Designed to get up and running quickly. 
Come with bootstrap[http://twitter.github.com/bootstrap/] installed with FontAwesome.  


### Usage

This assumes you have pip and django installed (if not, try `$ sudo easy_install pip`)

    $ django-admin.py startproject --template http://github.com/martinogden/django-boilerplate/zipball/master project_name
    $ pip install -r requirements.txt
    $ python manage.py syncdb --migrate


### Settings

There is a separate file for each environment inside `config/environments` (development, production). These import the django default settings from config.settings and are intended to be used directly, e.g. 

`python manage.py validate --settings=config.environments.production` 
						- or -  

`export PYTHONPATH=config.environments.development`.

Any settings added in `environments/local.py` will be picked up and override any previously defined settings. This is useful for sensitive information such as database credentials or the `SECRET_KEY` etc. By default this file will *NOT* be checked into git.

### Useful notes:
Command to freeze the current requirements of the enviroment and output as a .txt file.

pip freeze -E dev-env > requirements.txt

Likewise, a command to install current requirements to the virtualenv. 

pip install -E dev-env -r requirements.txt


### Credits

Full credits to Martin Ogden[https://github.com/martinogden] - This is a shameless rip from that repo. 

### TODOs

+Seperate less into bootstrap and custom?







