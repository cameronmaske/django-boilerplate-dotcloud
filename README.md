Adapted Django Boilerplate (Django 1.4 and DotCloud)
===========================================
A barebones default layout taken from [Martin Ogden's work](https://github.com/martinogden/django-boilerplate) and adapted for DotCloud (and a few personal likings).

Designed to get up and running quickly. 

Comes with [Bootstrap](http://twitter.github.com/bootstrap/) installed with [FontAwesome](http://fortawesome.github.com/Font-Awesome/).

### Usage
Note: I really recommand installing virtualenv (it makes your life easier).
First, make a directory for your project to be, then setup a a virtualenv inside (I like the name "dev-env").After that, pip install Django (1.4) and create a template based on this project. After all that, setup all the requirements and BAM, good to go. 

	$ mkdir my-project	
	$ cd my-project
	$ virtualenv --python=python2.7 dev-env
	$ source dev-env/bin/activate 
	$ pip install Django
    $ django-admin.py startproject --template https://github.com/cameronmaske/django-boilerplate-dotcloud/zipball/master project_name
    $ cd project_name
    Note: You need to rename your project's name at this point. Will figure out a better way to do this soon!
    $ mv rename_me desired_project_name
    $ pip install -r requirements.txt
    $ cd desired_project_name
    $ python manage.py syncdb
    $ python manage.py validate --settings=config.environments.development
    $ python manage.py runserver

Next, to deploy to Dotcloud, go through postinstall, nginx.conf and change {{ project_name }} to your app's name. 
Note: This is not elegant. I'll write a script soon to do all this. 


### Settings

There is a separate file for each environment inside `config/environments` (development, production). These import the django default settings from config.settings and are intended to be used directly, e.g. 

`python manage.py validate --settings=config.environments.production`
or 
`export PYTHONPATH=config.environments.development`.

Any settings added in `environments/local.py` will be picked up and override any previously defined settings. This is useful for sensitive information such as database credentials or the `SECRET_KEY` etc. By default this file will *NOT* be checked into git.

### Useful notes for DotCloud intergration:
Command to freeze the current requirements of the enviroment and output as a .txt file.

`pip freeze -E dev-env > requirements.txt`

Likewise, a command to install current requirements to the virtualenv. 

`pip install -r requirements.txt`

### Credits

Full credits to Martin Ogden for this great boilerplate (originally taken from https://github.com/martinogden) - This is a shameless rip from that repo. 

### TODOs
* Make the generic template more useful + pretty
* Write an install script. 
* Test the project out on DotCloud! 






