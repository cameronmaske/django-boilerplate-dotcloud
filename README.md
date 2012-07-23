Adapted Django Boilerplate (Django 1.4 and DotCloud)
===========================================
A barebones default layout taken from [Martin Ogden's work](https://github.com/martinogden/django-boilerplate) and adapted for DotCloud (and a few personal likings).

Designed to get up and running quickly. 

Comes with [Bootstrap](http://twitter.github.com/bootstrap/) installed with [FontAwesome](http://fortawesome.github.com/Font-Awesome/).

### How to install 
Simply download and run install.py and follow the various steps in your command line. 

    $ curl -o install.py https://raw.github.com/cameronmaske/django-boilerplate-dotcloud/master/install.py 
    $ python install.py

### Credits

Adapted by me! [Cameron Maske](http://www.cameronmaske.com). If this project helped, I've loved to hear about it! Give me a [tweet](https://twitter.com/cameronmaske)

### TODOs
* Complete the style guide /style/.
* Add optional user code/login support/waiting list to install.
* Add create development database + sync to install. 
* Add optional push to DotCloud to install.
* Tests! 

### Notes:
Any settings added in `environments/local.py` will be picked up and override any previously defined settings. This is useful for sensitive information such as database credentials or the `SECRET_KEY` etc. By default this file will *NOT* be checked into git.


