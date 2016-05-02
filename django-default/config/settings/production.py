from config.settings.base import *


DEBUG = False

ALLOWED_HOSTS = ['example.com']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': '', # Set to empty string for localhost.
    'PORT': '', # Set to empty string for default.
    }
}

ROOT_URLCONF = 'config.urls.production'
