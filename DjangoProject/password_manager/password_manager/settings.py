"""
Django settings for password_manager project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import django_heroku
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-if)wemw6fvea!b24p&c9$_%mafpf%qfn#ys_usx3_wuwd^!21w'

ENCRYPT_KEY = b'53M_ibOgPNhEQmiiPsmWviX_cPDXynb2hekEjaiRdrM='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


ALLOWED_HOSTS = ['pwm1-1008b3592347.herokuapp.com', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'frontend',
    'password_handler',
    'kagi',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'password_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Your custom templates directory
            BASE_DIR / 'kagi/kagi/templates',  # Correct path for Kagi's templates
],
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

WSGI_APPLICATION = 'password_manager.wsgi.application'


# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  # PostgreSQL database engine
#         'NAME': os.getenv('DB_NAME', 'pwmanagerdb'),  # Default DB name (use environment variable in production)
#         'USER': os.getenv('DB_USER', 'stang1'),  # Default DB user (use environment variable in production)
#         'PASSWORD': os.getenv('DB_PASSWORD', 'RDSdbpass1!'),  # Default DB password (use environment variable in production)
#         'HOST': os.getenv('DB_HOST', 'database-1.c1wkiqw2e7cx.us-east-1.rds.amazonaws.com'),  # Default DB host (use environment variable in production)
#         'PORT': os.getenv('DB_PORT', '5432'),  # Default PostgreSQL port
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'pwmanagerdb',
        'USER': 'stang1',
        'PASSWORD': 'RDSdbpass1!',
        'HOST': 'database-1.c1wkiqw2e7cx.us-east-1.rds.amazonaws.com',
        'PORT': '5432',  # default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static;'),)
django_heroku.settings(locals())

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# STATICFILES_DIRS = [
#     BASE_DIR / "static",  # Ensure Django looks here for static files
# ]
# STATIC_ROOT = BASE_DIR / 'staticfiles'  # Example path

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGOUT_REDIRECT_URL = 'homepage'  # Redirect to the homepage after logout
LOGIN_REDIRECT_URL = 'kagi:two-factor-settings'
LOGIN_URL = 'kagi:login'


INTERNAL_IPS = ['127.0.0.1']
RELYING_PARTY_ID = 'localhost'
RELYING_PARTY_NAME = 'Kagi Demo'
WEBAUTHN_ICON_URL = 'https://via.placeholder.com/150'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sophiamtran@gmail.com'
EMAIL_HOST_PASSWORD = 'srhl wlnj jkrd vqxt'  # Replace with your actual App Password


# Session timeout in seconds 
SESSION_COOKIE_AGE = 900

# Ensure session expires when the user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
