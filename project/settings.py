import os

import dj_database_url
from environs import Env


dotenv_path = os.path.join(os.path.dirname(__file__), '.env.private_settings')
private_settings = Env()
private_settings.read_env(dotenv_path)


DB_URL = private_settings('DB_URL')

DATABASES = {'default': dj_database_url.config(default=DB_URL)}

SECRET_KEY = private_settings.str('SECRET_KEY')

ALLOWED_HOSTS = private_settings('ALLOWED_HOSTS')

DEBUG = private_settings.bool('DEBUG')

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
