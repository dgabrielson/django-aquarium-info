"""
Django Project settings: demo_site
"""
#########################################################

import os  # for relative paths.

from django.conf.global_settings import *


def package_path(fragment):
    """
    Set up an absolute path relative to this file, pointing to the given fragment.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, fragment).replace('\\', '/')

#########################################################

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': package_path('demo_site.db'),
    }
}

TIME_ZONE = 'America/Winnipeg'
USE_TZ = True
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
SECRET_KEY = '$rjy%+3m6rh!6zs$y@=q5y)dyk+ax6e@n#&amp;07ddkk-=h7fnh7w'

USE_I18N = False
USE_L10N = True
ROOT_URLCONF = 'aquainfo.demo_site.urls'
WSGI_APPLICATION = 'aquainfo.demo_site.wsgi.application'

MEDIA_ROOT = package_path('__media')
MEDIA_URL = '/media/'
STATIC_ROOT = package_path('__static')
STATIC_URL = '/static/'
STATICFILES_DIRS += ('static', )
TEMPLATE_DIRS = ( package_path('templates'), )

INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin', 
    'django.contrib.admindocs', 
    
    'django.contrib.markup',
    'south',
    )

# other useful settings to augment:
# MIDDLEWARE_CLASSES
# TEMPLATE_CONTEXT_PROCESSORS

#########################################################

INSTALLED_APPS += ('gabrielson_standard', )
INSTALLED_APPS += ('aquainfo', )

#########################################################
