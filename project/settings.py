import os
from environs import Env


dotenv_path = os.path.join(os.path.dirname(__file__), '.env.database_params')
database_params = Env()
database_params.read_env(dotenv_path)

DATABASES = {
    'default': {
        'ENGINE': database_params.str('ENGINE'),
        'HOST': database_params.str('HOST'),
        'PORT': database_params.str('PORT'),
        'NAME': database_params.str('NAME'),
        'USER': database_params.str('DEFAULT_USER'),
        'PASSWORD': database_params.str('PASSWORD')
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = database_params.str('SECRET_KEY')

DEBUG = database_params.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


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
