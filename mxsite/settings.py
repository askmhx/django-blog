DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('menghx', 'mhxdev@gmail.com'),
)

MANAGERS = ADMINS

from bae.core import const
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'EZCrbFWAExhMsesUMomg',
        'USER': const.MYSQL_USER,
        'PASSWORD': const.MYSQL_PASS,
        'HOST': const.MYSQL_HOST,
        'PORT': const.MYSQL_PORT,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': const.CACHE_ADDR,
        'TIMEOUT':  60,
    }
}

#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

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
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\', '/'),)

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


TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

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