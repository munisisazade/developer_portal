# README #

# Developer Network #

### --- How to install and use for Linux ###

First you need to install python3 and after install django you can run the project following bellow steps
```
#!

$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
$ git clone https://github.com/munisisazade/developer_portal.git
$ cd developer_portal/
```

### --- Set up python3 evniroment ###
Create virtualenviroment for python3:
```
#!

$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Create the PostgreSQL Database and User:


```
$ sudo -u postgres psql
postgres=# CREATE DATABASE myproject;
postgres=# CREATE USER myprojectuser WITH PASSWORD 'password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
postgres=# \q
```
After all done this without errors you can use this project.
Run django server 

 ```
 $ python manage.py makemigrations
 $ python manage.py migrate
 $ python manage.py runserver
  Performing system checks...

  System check identified no issues (0 silenced).
  February 18, 2017 - 14:07:32
  Django version 1.10.5, using settings 'develop.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
 ```


----------------------------------------------------------------------------------------------------------------------------------------------------------------
# for Windows #


### --- How to install and use for Linux ###

install python3 for windows read this docs 
[python3 for windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)

### --- The development server ###

Change into the outer mysite directory, if you haven’t already, and run the following commands:
```
#!

$ python manage.py runserver
```

### --- Creating a project / app ###

Project: 
```
#!

$ django-admin startproject <myproject>
```
To create your **app**, make sure you’re in the same directory as manage.py and type this command: 
```
#!

$ python manage.py startapp <appname>
```



### --- Superuser ###

Create superusers using the createsuperuser command:
```
#!

$ python manage.py createsuperuser --username=joe --email=joe@example.com
```



### --- Migrate ###

By running **makemigrations**, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a *migration*.


```
#!

$ python manage.py makemigrations <appname>
```

Now, run **migrate** again to create those model tables in your database:


```
#!

$ python manage.py migrate
```


### --- Running tests ###

In the terminal, we can run our test:
```
#!
$ python manage.py test <appname>
```






### --- Shell ###

To invoke the Python shell, use this command:
```
#!
$ python manage.py shell
```


### --- Install dependencies ###

Installing required dependencies on virtual environment:
```
#!
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```



----------------------------------------------------------------------------------------------------------------------------------------------------------------

### --- Credits & Helpers ###
1. Extend your RAM by adding a swap file - http://stackoverflow.com/a/18335151/968751
1. Make ffmpeg executable everywhere - http://askubuntu.com/a/613799
1. FFMpeg permission denied error - http://askubuntu.com/a/478019
1. One liner ffmpeg (or other) to get only resolution? - http://askubuntu.com/a/577431 / http://stackoverflow.com/a/29585066 (json)
1. Revert to a commit by a SHA hash in Git? - http://stackoverflow.com/a/1895095

----------------------------------------------------------------------------------------------------------------------------------------------------------------

### --- Used modules & Apps ###
1. Media server: [ngnix RMTP](https://github.com/arut/nginx-rtmp-module)
1. Video edit: [ffmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)
