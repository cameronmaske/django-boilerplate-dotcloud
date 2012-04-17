import os, sys

if __name__ == '__main__':
	try:
		project_name = sys.argv[1]
	except:
		raise Exception("You didn't include an app_name. Such as python install.py project_name")
	if project_name:
		os.system("echo Configuring your django project [" + project_name + "]")
		os.system("echo Renaming project...")
		os.system("mv rename_me " + project_name)
		os.system("echo Installing requirements...")
		os.system("pip install -r requirements.txt")
		os.system("echo Setting up postinstall and nginx.conf")
		#Create postinstall
		f = open('postinstall', 'w')
		f.write('#! /bin/sh \npython ' + project_name + '/manage.py collectstatic --noinput \npython ' + project_name + '/manage.py syncdb --noinput \n')
		f.close()
		os.system("chmod +x postinstall")
		#Create nginx.conf
		f = open('nginx.conf', 'w')
		f.write('location /media/ {root /home/dotcloud/current/%s/public/media ;} \nlocation /static/ {root /home/dotcloud/current/%s/public/static; }' % (project_name, project_name))
		f.close()
		os.system("echo Postinstall and nginx.conf created")
		os.system("python %s/manage.py syncdb" % project_name)
		os.system("python %s/manage.py validate --settings=config.environments.development" % project_name)
		os.system("echo Looked like everything worked! Try going to 127.0.0.1:8000 to confirm.")
		os.system("echo Starting up the server now...")
		os.system("echo Happy developing!")
		os.system("python %s/manage.py runserver" % project_name)
