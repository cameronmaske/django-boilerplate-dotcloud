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

if __name__ == '__main__':
	path = os.getcwd()
	#We get the user to input the desired app name. 
	print "Let's setup your app! "
	app_name = raw_input("Enter the app's name.\n This will be shared with both DotCloud and Django.\n ")
	
	#Next, we setup the virtualenv. 
	#Let's deactivate any virtualenv currently set. 
	#os.system("deactivate")
	print "Creating the app '%s' directory and virtual enviroment." % app_name
	os.system('virtualenv --python=python2.7 %s' % app_name)
	print "Changing directory to %s/%s" % (path,app_name)
	os.chdir("%s/%s/" % (path,app_name))
	print "Activating the virtual enviroment."
	os.system("source bin/activate")

	#Now we setup Django.
	print "Installing Django, please hold."
	os.system("pip install django")
	#Note: At this point, we should check that the name is valid. https://github.com/django/django/blob/master/django/core/management/commands/startproject.py
	print "Django has been installed."

	#We create the template project for our django app. 
	print "Creating a new django project boilerplate. Don't worry you can customize it soon enough. "
	#Runs an uber startproject. Should access all files with the extension tag, and create the project within the current directory. 
	os.system('django-admin.py startproject --template https://github.com/cameronmaske/django-boilerplate-dotcloud/zipball/master %s --extension py,md,conf,yml .' % app_name)
	

	#Let's start the customization. 
	#Do we include DotCloud support?
	decision = query_yes_no("\nDo you want to include DotCloud support?")
	if decision:
		print "Setting up DotCloud. Creating and chmod'ing postinstall. "

		#Create postinstall.
		f = open('postinstall', 'w')
		#Populates it. 
		f.write('#! /bin/sh \npython ' + app_name + '/manage.py collectstatic --noinput \npython ' + app_name + '/manage.py syncdb --noinput \n')
		f.close()
		#Chmod it. 
		os.system("chmod +x postinstall")
	#Else, we need to remove dotcloud files
	else:
		print "Removing DotCloud specific files."
		os.system("rm dotcloud.yml")
		os.system("rm nginx.conf")
		os.system("rm postinstall")

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





