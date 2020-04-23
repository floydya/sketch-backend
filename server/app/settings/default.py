import datetime
import os

import environ
import jinja2
from pathlib import Path

from django_jinja.builtins import DEFAULT_EXTENSIONS
from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__)
BASE_ROOT = BASE_DIR.parent.parent

env = environ.Env(DEBUG=(bool, False), )

env_file = str(BASE_ROOT.parent / '.env')
env.read_env(env_file)

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG') == "True"
ALLOWED_HOSTS = list()

INSTALLED_APPS = (
    'cacheops',
    'phonenumber_field',
    'rosetta',
    'django_jinja',
    'solo',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
    'djmoney',
    'rest_framework_swagger',
    # 'mptt',
    'crispy_forms',
    'jet',
    'djoser',
    # 'django_celery_beat',

    'postie',
    'codemirror2',
    'ckeditor',
    'des',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'debug_toolbar',

    'applications.accounts',
    'applications.transactions',
    'applications.notifications',
)

JQUERY_URL = False
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ('127.0.0.1',)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'NAME': 'jinja2',
        'APP_DIRS': True,
        'DIRS': [],
        'OPTIONS': {
            'environment': 'shared.env.jinja2.environment',
            'match_extension': '.jinja',
            'newstyle_gettext': True,
            'auto_reload': True,
            'undefined': jinja2.Undefined,
            'debug': True,
            'filters': {},
            'globals': {},
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'extensions': DEFAULT_EXTENSIONS,
            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": True,
            },
        },
    },
    {
        'DIRS': [os.path.join(BASE_ROOT.parent, 'markup', 'templates')],
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': env.db('DJANGO_DB_URL')
}
DATABASES['default']['CONN_MAX_AGE'] = None
DATABASES['default']['DISABLE_SERVER_SIDE_CURSORS'] = True

AUTH_USER_MODEL = 'accounts.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'des.backends.ConfiguredEmailBackend'
POSTIE_HTML_ADMIN_WIDGET = {
    "widget": "CKEditorWidget",
    "widget_module": "ckeditor.widgets",
    "attrs": {"attrs": {"cols": 80, "rows": 10}}
}
POSTIE_INSTANT_SEND = True

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-US'
LANGUAGES = (
    ('en-US', _('English')),
)
LOCALE_PATHS = (
    BASE_ROOT / 'locale',
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_DJANGO_JQUERY = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_ROOT / 'static'

MEDIA_URL = '/uploads/'
MEDIA_ROOT = BASE_ROOT / 'uploads'

SITE_ID = 1
CACHES = {
    'default': env.cache_url('DJANGO_CACHE_URL', 'dummycache://127.0.0.1')
}
SOLO_CACHE = "default"

CACHEOPS_REDIS = "redis://cache:6379/1"
CACHEOPS = {
    'accounts.*': {'ops': 'all', 'timeout': 60 * 15},
    'transactions.*': {'ops': 'all', 'timeout': 60 * 60},
    'notifications.*': {'ops': 'all', 'timeout': 60 * 60},
    '*.*': {'ops': (), 'timeout': 60 * 60},
}

CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'EXCEPTION_HANDLER': 'shared.exception.custom_exception_handler'
}

JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=36000),
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 1024

FILTERS_NULL_CHOICE_LABEL = True
DEFAULT_CURRENCY = "USD"
CURRENCIES = ('USD',)
CURRENCY_CHOICES = [('USD', 'USD $')]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda x: DEBUG,
}
JET_CHANGE_FORM_SIBLING_LINKS = False

STRINGS = {
    'REQUIRED': _("This field is required."),
}
DJOSER = {
    "SERIALIZERS": {
        'current_user': 'applications.accounts.api.serializers.UserSerializer'
    },
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "ACTIVATION_URL": "http://localhost:3000/auth/activate/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "http://localhost:3000/auth/password-reset/{uid}/{token}"
}
