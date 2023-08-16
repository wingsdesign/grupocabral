import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

SECRET_KEY = 'django-insecure-#m7*9j03vdg9vjkcfynb74zvb@1(7-dwn2u^1&197cfwp=s_-2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.3.17']

ADMINS = (
    ('Sancley Alhadef', 'sancleydesign@gmail.com'),
    
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # MEUS APPS
    'grupocabral.filiais',
    'grupocabral.noticias',
    'grupocabral.contato',

    # APPS GLOBAIS
    'colorfield',
    'ckeditor',
    'rest_framework',
    
]

THOUSAND_SEPARATOR='.',
USE_THOUSAND_SEPARATOR=True

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads"
CKEDITOR_ALLOW_NONIMAGE_FILES = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grupocabral.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'grupocabral.context_processors.grupocabral',
            ],
        },
    },
]

WSGI_APPLICATION = 'grupocabral.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Araguaina'

USE_I18N = True

USE_TZ = True

USE_L10N = True

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

#===== STATIC IN PRODUÇÃO =====
# MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "media"), )
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')


import smtplib

DEFAULT_EMAIL_FROM = 'site.grupocabral@gmail.com'
EMAIL_USE_LOCALTIME = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'site.grupocabral@gmail.com'
EMAIL_HOST_PASSWORD = 'efpvbreklmsghjxy'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
