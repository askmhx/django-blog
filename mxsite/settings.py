DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('menghx', 'mhxdev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
        'CHARSET': 'utf8',
        'COLLATION': 'utf8_general_ci',
        'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'},
    }

}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

ALLOWED_HOSTS = ['blog.iosxc.com']

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'en_us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'Y-m-d'

DATE_INPUT_FORMATS = ('%Y-%m-%d',)

DATETIME_FORMAT = 'Y-m-d H:M:S'

DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%M:%S', )

import os

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = '/var/projects/mxsite/static'

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = '&!+*ecyg7us9os231%@z__b9lm%6%+_j8o)z4zy6c)!^itl^ph'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mxsite.urls'

WSGI_APPLICATION = 'mxsite.wsgi.application'


TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'ckeditor',
    'mxblog',
)

CKEDITOR_UPLOAD_PATH = os.path.join(STATIC_ROOT, 'uploads')
CKEDITOR_SLUGIFY_FILENAME = False
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 600,
        'width': 1000,
    },
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

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

AUTH_USER_MODEL = 'mxblog.PostUser'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'