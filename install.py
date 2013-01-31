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
	valid = {"yes": True, "y": True, "Y":True, 
			"no": False, "n":False, "N": False}

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
	#We get the user to input the desired app name. 
	print "Let's setup your app! "
	app_name = raw_input("Enter the app's name.\n"
		"This will be shared with both DotCloud and Django.\n")
	app_path = "%s/%s" % (path,app_name)

	#A bit of fun. 
	print "And so it shall be, that %s will be created!" % app_name
	#Next, we setup the virtualenv. 
	print "Creating the app '%s' directory and virtual enviroment." % app_name
	#Is there a way to share agurements when formatting strings?
	os.system('virtualenv --python=python2.7 %s' % app_name)

	#Creating the enviroment path. 
	#Need to create global variables (odd in python huh!).
	#This is due to os.system creating a sub-shell each time it is called. 
	#This may not be the ideal solution, but it works for now. 
	print "Activating the virtual enviroment."
	global env_path 
	env_path = "%s/bin/activate" % app_path
	#Try to get around bash/other-shell discrepancies.
	bash = query_yes_no("By the way, are you using bash right now?")
	global env_activate
	env_activate = ("." if bash else "source") + " " + env_path

	#Next, we cd into the project's folder. 
	print "Changing directory to %s/%s" % (path,app_name)
	os.chdir(app_path)

	#Now we setup Django.
	version = raw_input("What version of Django? [Default 1.4.3]")
	version = version or "1.4.3"
	print version
	print "Installing Django, please hold."
	virtualenv("pip install django==%s" % version)
	#Note: At this point, we should check that the name is valid.
	#https://github.com/django/django/blob/master/django/core/management/commands/startproject.py
	print "Django has been installed."

	#We create the template project for our django app. 
	print "Creating a new django project boilerplate. Don't worry you can customize it soon enough. "
	#Runs an uber startproject. Should access all files with the extension tag, and create the project within the current directory. 
	virtualenv('django-admin.py startproject --template https://github.com/cameronmaske/django-boilerplate-dotcloud/zipball/master %s --extension py,md,conf,yml .' % app_name)
	

	#Let's start the customization. 
	#Do we include DotCloud support?
	decision = query_yes_no("\nDo you want to include DotCloud support?")

	#If so, we need to setup postinstall. 
	if decision:
		print "Setting up DotCloud. Creating and chmod'ing postinstall. "

		#Updates postinstall.
		replace_line_re("postinstall", "{{ project_name }}", app_name)
		#Chmod it. 
		os.system("chmod +x postinstall")

	#Else, we need to remove dotcloud files
	else:
		print "Removing DotCloud specific files."
		os.system("rm dotcloud.yml")
		os.system("rm nginx.conf")
		os.system("rm postinstall")
		os.system("rm wsgi.py")

	#Do you want to include user support?
	decision = query_yes_no("\nDo you want to setup user support?")
	if decision:
		pass
		#replace_line_re("%s/config/settings.py", "#User setup", "userena")

	#Do you want to login with twitter?
	decision = query_yes_no("\nDo you want to include Twitter for logging in?")
	if decision:
		pass
		#replace_line_re("%s/config/settings.py", "#Twitter login", "allauth")

	#Do you want to include a beta waiting?
	decision = query_yes_no("\nDo you want to setup a beta waiting list?")
	if decision:
		pass
		#replace_line_re("%s/config/settings.py", "#Beta waiting", "waiting")


	#Finishing off the install. 
	print "Removing redudant files used for install"
	#Removes redudant files, such as our install script. 
	os.system("rm install.py")
	os.system("rm install2.py")

	#Let's create a nice template README.md for the project. 
	#In the future hopefully this will be more robust, include the project's name and written better. 
	#For now it will do. 
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

	#Now we have to install all the requirements to the virtualenv before we can setup the app in development. 
 	print "Install requirements.txts"
	virtualenv("pip install -r requirements.txt")

	#After the setup of the files, let's run the project. 
	print "Let's get a database up in here. Sync'in the DB"
	virtualenv("python %s/manage.py syncdb" % app_name)

	print "Now let's run the server! Happy developing!"
	virtualenv("python %s/manage.py runserver&" % app_name)
	# - syncdb
	# - migrate -all (south)
	# - validate --settings=config.enviroment
	# - runserver& (in the background)

	#Finally, give the user the option to push to dotcloud. 
	decision = query_yes_no("\nDo you want to push the app to DotCloud?")
	# - create a new dotcloud app. 
	# - push the app. 

	# Fin! #




