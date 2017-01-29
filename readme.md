# Local run

To run the project locally

* clone repo
* `cd massive_csv/`  
* `virtualenv venv`  
* `source venv/bin/activate`  
* `pip install -r requirements.txt`  
* create file `massive_csv/local_settings.py` and fill like in example below   
* create database, user, grant perms to user  
* run migrations `./manage.py migrate` and wait

**Development local_settings.py example**

    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dbname',
            'USER': 'dbuser',
            'PASSWORD': 'dbpassword',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


