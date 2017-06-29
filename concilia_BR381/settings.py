# coding=utf-8
"""

Criado por @lucaslamounier - 2017


Github: https://github.com/lucaslamounier

Django settings for concilia_BR381 project.

"""

import os
import sys
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#ekp!1d6i43o2b+2o9vz3jhn)f$*k8c=b8%-(&=+5^kf!lau^p'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # Libs
    'sortedm2m',
    'widget_tweaks',
    'easy_thumbnails',

    # Local Apps
    'core',
    'content',
    'photologue',
    'redactor',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'concilia_BR381.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # apps
                'content.context_processors.comunidades',
            ],
        },
    },
]


WSGI_APPLICATION = 'concilia_BR381.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.rondon'),
    }
}

# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, r'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

# E-mail
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'admin@dnit.gov.br'

# messages
from django.contrib.messages import constants as messages_constants
MESSAGE_TAGS = {
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

# Redactor settings

REDACTOR_OPTIONS = {'lang': 'pt_br', 'focus': False, 'wym': False,
                    'plugins': ['alignment', 'fullscreen', 'fontsize',
                                'fontcolor', 'fontfamily', 'video',
                                'textdirection', 'inlinestyle', 'table',
                                'imagemanager', 'filemanager', 'textexpander']}

REDACTOR_UPLOAD = 'noticias/redactor/uploads/'

# Heroku settings
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'timeline_images': {'size': (250, 220), 'crop': True},
        'home_news': {'size': (300, 200), 'crop': True},
        'home_videos': {'size': (470, 290), 'crop': True},
        'galery_detail': {'size': (220, 165), 'crop': True},
    },
}

# YOUTUBE API
YOUTUBE_API_KEY = 'AIzaSyApRzZncaa999A5WClkrCpCAXleNDec4Zc'

# LOGGING CONFIGURATION
# A logging configuration that writes log messages to the console.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     # Formatting of messages.
#     'formatters': {
#         # Don't need to show the time when logging to console.
#         'console': {
#             'format': '%(levelname)s %(name)s.%(funcName)s (%(lineno)d) %(message)s'
#         }
#     },
#     # The handlers decide what we should do with a logging message - do we email
#     # it, ditch it, or write it to a file?
#     'handlers': {
#         # Writing to console. Use only in dev.
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         },
#         # Send logs to /dev/null.
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#     },
#     # Loggers decide what is logged.
#     'loggers': {
#         '': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'photologue': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         # logging of SQL statements. Default is to ditch them (send them to
#         # null). Note that this logger only works if DEBUG = True.
#         'django.db.backends': {
#             'handlers': ['null'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }

# Don't display logging messages to console during unit test runs.
# if len(sys.argv) > 1 and sys.argv[1] == 'test':
#     LOGGING['loggers']['']['handlers'] = ['null']
#     LOGGING['loggers']['photologue']['handlers'] = ['null']

# Local Settings
try:
    from .local_settings import *
except ImportError:
    pass
