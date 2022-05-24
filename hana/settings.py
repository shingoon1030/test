import os
import django_heroku
from pathlib import Path
from django.contrib.messages import constants as messages_constants

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-(pu!y)*rq&a^+o246ql))_mq5owpn+=exsqk*1m-id%7&5q4!6'
DEBUG = True
ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'account.User'
MESSAGE_LEVEL = messages_constants.DEBUG

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'django.contrib.humanize',
    'account',
    'homeapp',
    'freeboard',
    'questionboard',
    'lectureboard',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'hana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'hana/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hana.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/' 
STATICFILES_DIRS = [ BASE_DIR/'static', os.path.join(BASE_DIR, 'static') ]
STATIC_ROOT = os.path.join('staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = "/media/"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.naver.com'
EMAIL_HOST_USER = 'has_everytime'
EMAIL_HOST_PASSWORD = 'saniza1030'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
DEFAULT_FROM_MAIL = 'has_everytime@naver.com'