import json

from django.core.exceptions import ImproperlyConfigured

with open("secret.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} enviroment variable"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")


#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': get_secret("database-name"), #2
        'USER': get_secret("database-user"), #3                      
        'PASSWORD': get_secret("database-pw"),  #4              
        'HOST': get_secret("database-host"),   #5                
        'PORT': '3306', #6
    }
}