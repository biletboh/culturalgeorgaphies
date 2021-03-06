"""
Django settings for cultg project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
conf = configparser.ConfigParser()
conf.read(os.path.join(BASE_DIR, 'settings.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*)10&!ms&t(=$bi=1sr4m8saf6vmdp@4@nsydiy1*kj1wf^yzu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf.getboolean('cultg', 'debug', fallback = True)

ALLOWED_HOSTS = ['*']

#Tumnails settings 
THUMBNAIL_ALIASES = {
    '': {
        'extra_small': {'size':(45, 45), 'crop': True},
        'small': {'size':(60, 60), 'crop': True},
        'medium': {'size': (750, 450), 'crop': True},
        'large': {'size': (800, 550), 'crop': True},
        'extra_large': {'size': (1200, 600), 'crop': True},
        },
    }
THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'

# Application definition

INSTALLED_APPS = [
    'cgapp.apps.CgappConfig',
    'grappelli',
    'filebrowser',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'django_file_form',
    'django_file_form.ajaxuploader',
    'widget_tweaks',
    'el_pagination',
    'datetimewidget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #timezones middleware
    'cgapp.middleware.tz_middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'cultg.urls'

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
                ]
            },
    },
]

#Loggin of errors on production
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            # Include the default Django email handler for errors
            # This is what you'd get without configuring logging at all.
            'mail_admins': {
                'class': 'django.utils.log.AdminEmailHandler',
                'level': 'ERROR',
                # But the emails are plain text by default - HTML is nicer
                'include_html': True,
                },
            # Log to a text file that can be rotated by logrotate
            'logfile': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(BASE_DIR, 'cultg.log')
                },
            },
        'loggers': {
            # Again, default Django configuration to email unhandled exceptions
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            # Might as well log any errors anywhere else in Django
            'django': {
                'handlers': ['logfile'],
                'level': 'ERROR',
                'propagate': False,
                },
            # Your own app - this assumes all your logger names start with "myapp."
            'cultg': {
                'handlers': ['logfile'],
                'level': 'WARNING', # Or maybe INFO or DEBUG
                'propagate': False
                },
            },
        }

WSGI_APPLICATION = 'cultg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

CURRDB = {'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}

if DEBUG is False:
    CURRDB = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conf.get('cultg', 'dbname', fallback = 'cultg'),
        'USER': conf.get('cultg', 'dbuser', fallback = 'postgres'),
        'PASSWORD': conf.get('cultg', 'dbpass', fallback = 'postgres'),
        'HOST': 'localhost',
        'PORT': '5432' 
        }

DATABASES = {
    'default': CURRDB
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Locale settings
LANGUAGES = (
        ('en', 'English'),
        ('uk', 'Ukrainian'),
)

LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#TinyMCE config
TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/static/tiny_mce'

TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
        'plugins': 'advlist,autolink,autoresize,emotions,fullpage,fullscreen,media,table,spellchecker,paste,searchreplace,wordcount',
        'theme': "advanced",
        'theme_advanced_resizing': True,
        'theme_advanced_resize_horizontal': True,
        'theme_advanced_buttons1': 'undo,redo,fontselect,fontsizeselect,bold,italic,underline,strikethrough,|,forecolor,backcolor,|,bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,|,outdent,indent,|,link,unlink,|,image,media,|,emotions,blockquote,|,table,hr,sub,sup,charmap',
        'theme_advanced_buttons2' : "",
        'width': '100%',
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
        }
TINYMCE_COMPRESSOR = False 
TINYMCE_FILEBROWSER = True 

LOGIN_REDIRECT_URL = '/dashboard/news/add/'
