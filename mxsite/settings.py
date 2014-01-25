
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('menghx', 'mhxdev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rBcccWonJFYwDiFYWvlJ',
        'USER': 'EScaDGFFmMBaEicRacLFBA90',
        'PASSWORD': 'UlWUCIoINM35T40q0Ug2lwQKXV7rkXno',
        'HOST': 'sqld.duapp.com',
        'PORT': '4050',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'Y-m-d'

DATE_INPUT_FORMATS = ('Y-m-d',)

DATETIME_FORMAT = 'Y-m-d'
#DATETIME_FORMAT = 'Y-m-d H:M:S'

DATETIME_INPUT_FORMATS = ('Y-m-d H:M:S', )

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

import os
from django.contrib import admin
STATICFILES_DIRS = [os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\', '/'),
                    os.path.join(os.path.dirname(admin.__file__), 'static')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = '=f@ar1vc4x0tc15i3j)k&ccct@w-!!67hv!0o=z^hftn)cg!+l'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mxsite.urls'

WSGI_APPLICATION = 'mxsite.wsgi.application'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\', '/'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'ckeditor',
    'mxblog',
)

CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), '..', 'static/ufiles').replace('\\', '/')
CKEDITOR_UPLOAD_PREFIX = "http://blog.vcher.com/static/ufiles/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 600,
        'width': 1000,
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}