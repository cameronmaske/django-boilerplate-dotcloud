# coding: utf-8
import os, sys, re, fileinput

def replace_line(file, original, new):
	for line in fileinput.input(file):
		line = line.replace(original, new)

def replace_line_re(file, original, new):
	data = open(file).read()
	o = open(file, "w")
	o.write(re.sub(original, new, data))
	o.close

def query_yes_no(question):
	#Based on http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input
	"""
	Ask a yes/no question via raw_input and return their answer.

   	"question" - is a string that is presented to the user.
    "default" - is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".

	"""
	valid = {"yes": True, "y": True, "Y": True, 
			"no": False, "n": False, "N": False}

	prompt = "[y/n]: "

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'Y' or 'N'\n")

def virtualenv(command):
	os.system(env_activate + '&&' + command)

if __name__ == '__main__':
	path = os.getcwd()
	app_name = raw_input("Enter the app's name.\n"
		"This will be shared with both DotCloud and Django.\n")
	app_path = "%s/%s" % (path,app_name)

	print "And so it shall be, that %s will be created!" % app_name
	print "Creating the app '%s' directory and virtual enviroment." % app_name
	os.system('virtualenv --python=python2.7 %s' % app_name)

	#Creating the enviroment path. 
	#Need to create global variables (odd in python huh!).
	#This is due to os.system creating a sub-shell each time it is called. 
	#This may not be the ideal solution, but it works for now. 
	print "Activating the virtual enviroment."
	global env_path 
	env_path = "%s/bin/activate" % app_path
	bash = query_yes_no("By the way, are you using bash right now?")
	global env_activate
	env_activate = ("." if bash else "source") + " " + env_path

	#Next, we cd into the project's folder. 
	print "Changing directory to %s/%s" % (path,app_name)
	os.chdir(app_path)

	version = raw_input("What version of Django? [Default 1.4.3]")
	version = version or "1.4.3"
	print version
	print "Installing Django, please hold."
	virtualenv("pip install django==%s" % version)
	print "Django has been installed."

	#We create the template project for our django app. 
	print "Creating a new django project boilerplate. Don't worry you can customize it soon enough. "
	#Runs an uber startproject. Should access all files with the extension tag,
	# and create the project within the current directory. 
	template_url = "https://github.com/cameronmaske/django-boilerplate-dotcloud/zipball/master"
	virtualenv('django-admin.py startproject --template '
		'%s %s --extension py,md,conf,yml .' % (template_url, app_name))

	#Let's start the customization. 
	#Do we include DotCloud support?
	dotcloud = query_yes_no("\nDo you want to include DotCloud support?")

	#If so, we need to setup postinstall. 
	if dotcloud:
		print "Setting up DotCloud. Creating and chmod'ing postinstall. "
		#Updates postinstall.
		replace_line_re("postinstall", "{{ project_name }}", app_name)
		#Chmod it. 
		os.system("chmod +x postinstall")
	else:
		print "Removing DotCloud specific files."
		os.system("rm dotcloud.yml")
		os.system("rm nginx.conf")
		os.system("rm postinstall")
		os.system("rm wsgi.py")

	print "Removing redudant files used for install"
	os.system("rm install.py")
	os.system("rm install2.py")

	print "Creating a fresh README.md"
	file = open('README.md', 'w')
	file.write(
	"""
	This is a main heading.
	==============

	This is a sub heading
	--------------

	*This is Italics*

	**This is Bold**

	- This is list item
	- This is list item

		An indent will end up as code

	Not sure what to put in a README.md?
	--------------
	*[This may help](http://stackoverflow.com/questions/2304863/how-to-write-a-good-readme)*
	"""
	)
	file.close()

 	print "Install requirements.txts"
	virtualenv("pip install -r requirements.txt")

	print "Let's get a database up in here. Sync'ing the DB"
	virtualenv("python %s/manage.py syncdb" % app_name)

	print "Now let's run the server! Happy developing!"
	virtualenv("python %s/manage.py runserver&" % app_name)