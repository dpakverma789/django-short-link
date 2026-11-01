from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['.vercel.app', '.now.sh']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME_PROD"),
        'USER': os.getenv("DB_USER_PROD"),
        'PASSWORD': os.getenv("DB_PASSWORD_PROD"),
        'HOST': os.getenv("DB_HOST_PROD"),
        'PORT': os.getenv("DB_PORT_PROD", "5432"),
    }
}

# HTTPS SETTINGS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 3153600
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS =True