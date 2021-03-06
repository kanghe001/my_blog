# coding=utf-8
"""
Django settings for MyBlog_project project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_m%$(+h4y$c0^035#b0z@-au98lccaoui!*k1o1vw)far=u!z3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'standard': {
                 'format': '%(levelname)s %(asctime)s %(message)s'
                 },
     },
     'filters': {
     },
     'handlers': {
         'mail_admins': {
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler',
             'formatter':'standard',
         },
         'test1_handler': {
             'level':'DEBUG',
             'class':'logging.handlers.RotatingFileHandler',
             'filename':'path1',
             'formatter':'standard',
         },
         'test2_handler': {
             'level':'DEBUG',
             'class':'logging.handlers.RotatingFileHandler',
             'filename':'path2',
             'formatter':'standard',
         },
     },
     'loggers': {
         'django.request': {
             'handlers': ['mail_admins'],
             'level': 'ERROR',
             'propagate': True,
         },
         'test1':{
             'handlers': ['test1_handler'],
             'level': 'INFO',
             'propagate': False
         },
         'test2':{
             'handlers': ['test2_handler'],
             'level': 'INFO',
             'propagate': False
         },
     }
}


ALLOWED_HOSTS = []

WEB_SITE = 'www.MyBlog.com'
WEB_TITLE = '我是猪的部落格'
WEB_SIGNAL = '梦虽虚幻,却是自己的梦想；位虽低微,却是自己的岗位；屋虽简陋,却是自己的家；志虽渺小,却是自己的追求。'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'MyBlog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'my_blog.views.global_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyBlog_project.wsgi.application'
AUTH_USER_MODEL = 'my_blog.User'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'kanghe19911027',

    }
}

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'static'),
)
