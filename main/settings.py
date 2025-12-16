from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jq_ppz)9@$n_5o%)yyy&mohc!0j(3c-0#87q^j+bmt_4%zt_4='

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'rest_framework.authtoken',
    'users',
    'product',
    'django_celery_beat',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'
# drf-spectacular конфигурация
SPECTACULAR_SETTINGS = {
    'TITLE': 'Custom User API',
    'DESCRIPTION': 'API для управления пользователями с кастомной моделью',
    'VERSION': '1.0.0',
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
}

# JWT конфигурация
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

CACHES = {


    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"
CELERY_BEAT_SCHEDULE = {
    # Задача #1: Очистка старых файлов (каждый день в 3:00)
    'cleanup-old-temp-files': {
    'cleanup-old-temp-files': {
        'task': 'users.tasks.cleanup_old_temp_files',
        'schedule': crontab(hour=3, minute=0),
    },
    
    'deactivate-inactive-users': {
        'task': 'users.tasks.deactivate_inactive_users_task',
        'schedule': crontab(hour=2, minute=0),
    },
    
    'send-daily-report': {
        'task': 'users.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=0),
    },
    
    'test-cleanup-every-minute': {
        'task': 'users.tasks.cleanup_old_temp_files',
        'schedule': crontab(minute='*/1'),
    },
}

EMAIL_BACKEND = 'django.core.mail.backends. console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sagynbaevaman7.09@gmail.com'
DEFAULT_FROM_EMAIL = 'sagynbaevaman7.09@gmail.com'
EMAIL_HOST_PASSWORD = 'aman.10.03.2008'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = 'admin@example.com'
