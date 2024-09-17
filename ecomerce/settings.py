"""
Django settings for ecomerce project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ
import os
import dj_database_url
env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'environ',
     "crispy_forms",
    "crispy_bootstrap5",
    'rest_framework',
    'api',
    'rest_framework.authtoken'
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

ROOT_URLCONF = 'ecomerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'ecomerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

""" DATABASES = {
    'default': dj_database_url.config(
            default=env('DATABASE_URL')
        )
}  """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





# Replace the DATABASES section of your settings.py with this
""" DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('PGDATABASE'),
    'USER': env('PGUSER'),
    'PASSWORD': env('PGPASSWORD'),
    'HOST': env('PGHOST'),
    'PORT': env('PGPORT'),
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}



 """







# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS =[ os.path.join(BASE_DIR,'static')]
MEDIA_URL = 'media/'


CLOUNDFLARE_R2_BUCKET=env('CLOUNDFLARE_R2_BUCKET')
CLOUNDFLARE_R2_ACCESS_KEY=env('CLOUNDFLARE_R2_ACCESS_KEY')
CLOUNDFLARE_R2_SECRET_KEY=env('CLOUNDFLARE_R2_SECRET_KEY')
CLOUNDFLARE_R2_BUCKET_ENDPOINT=env('CLOUNDFLARE_R2_BUCKET_ENDPOINT')

CLOUNDFLARE_R2_CONFIG_OPTIONS = {
    'bucket_name':CLOUNDFLARE_R2_BUCKET,
    'access_key':CLOUNDFLARE_R2_ACCESS_KEY,
    'secret_key':CLOUNDFLARE_R2_SECRET_KEY,
    'endpoint_url':CLOUNDFLARE_R2_BUCKET_ENDPOINT,
    'default_acl': 'public-read', # private
    'signature_version': 's3v4',

}

STORAGES = {
    'default': {
        "BACKEND":'helpers.cloundflare.storages.MediaFilesStorage',
        "OPTIONS":CLOUNDFLARE_R2_CONFIG_OPTIONS
    },
    'staticfiles':{
        "BACKEND":'helpers.cloundflare.storages.StaticFilesStorage',
        "OPTIONS":CLOUNDFLARE_R2_CONFIG_OPTIONS
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"



DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
LOGIN_REDIRECT_URL = '/login' # -> somethign is wrong here ??


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}