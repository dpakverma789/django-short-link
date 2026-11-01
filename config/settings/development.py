from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','192.168.1.6']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME_LOCAL"),
        'USER': os.getenv("DB_USER_LOCAL"),
        'PASSWORD': os.getenv("DB_PASSWORD_LOCAL"),
        'HOST': os.getenv("DB_HOST_LOCAL"),
        'PORT': os.getenv("DB_PORT_LOCAL", "5432"),
    }
}