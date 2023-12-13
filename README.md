## Task Management | Backend

### Installation 
First ensure you have python globally installed in your computer. If not, you can get python [here](https://python.org).

### Install IDE
Install VisualStudio Code in your computer. Use the [this](https://code.visualstudio.com/download) link to install VisualStudio Code.

### Setup

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv

Then, Git clone this repo to your PC

    $ git clone - git clone **url
    $ cd task_management
    
### Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
### Install dependancies

    $ pip install -r requirements.txt

### Create a .env file inside task_management folder & this file must consist the following keys--
environment="development"

### Place the following file inside configuration folder

    1.development.py
    2.production.py


### values for development.py file

#configuration credentials
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#DATABASE CREDENTIALS

DATABSE_CONFIG={
    'ENGINE': 'django.db.backends.mysql',
    'NAME':'',
    'USER' :'',
    'PASSWORD' :'',
    'HOST' :'localhost',
    'PORT' :'3306',
}

#EMAIL CREDENTIALS

EMAIL_CONFIG={    
    'EMAIL_BACKEND':'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_HOST' :'smtp.gmail.com',
    'EMAIL_USE_TLS':True,
    'EMAIL_PORT' :587,
    'EMAIL_HOST_USER' :"",
    'EMAIL_HOST_PASSWORD':"",
    'DEFAULT_FROM_EMAIL' :"",
}

SECERET_KEYS ='django-insecure-ymtq$6w-9dcj(zybf$buf&6z$s+sh#w3fb$*@_#y*7xu8rp8q1'
   
CONFIG={
    "ALLOWED_HOST":'[*]',
    "LOGO_PATH":"",
    "PYTHON_PATH":"",
    "BASE_PATH":BASE_DIR,
    "LANGUAGE_CODE":"en-us",
    "TIME_ZONE":"UTC",
    "STATIC_URL":"static/",
    "USE_I18N":True,
    "USE_TZ":True,
    "log_path":os.path.join(BASE_DIR, 'Log')
}

IP_CONFIG=['127.0.0.01','132.1.2.2']
ALLOWED_COUNTY=['IN','AUS','US','UK','RSA']

TIME_ZONE ="IND"

#ADMIN DEATILS FOR CREATE A SUPERADMIN

ADMIN_EMAIL ="admin@gmail.com"
ADMIN_USERNAME="admin"

SERVER_URL="http://127.0.0.1:8000/"


    
<!-- Make migrations & migrate -->

    $ python manage.py makemigrations && python manage.py migrate

<!-- Then we have to add master datas in database  -->
    1.Super User
    

<!-- Commands to create above datas: -->
    1.python manage.py createsuperuser


### Launching the app
    $ python manage.py runserver

    $ click http://127.0.0.1:8000 & change the link to http://127.0.0.1:8000/tasks/ in browser





