import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'key'

DEBUG = True

ALLOWED_HOSTS = ['*']






DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'USER': 'dg',
        'PASSWORD': '11111111',
        'HOST': 'localhost'
    }
}










STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATIC_URL = '/static/' 

MEDIA_URL = '/media/'


