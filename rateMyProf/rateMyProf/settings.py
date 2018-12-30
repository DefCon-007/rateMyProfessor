"""
Django settings for rateMyProf project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import configparser
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import json
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(BASE_DIR + "/config.ini")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("core", "SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean("core", "DEBUG")
ALLOWED_HOSTS = config.get("core", "ALLOWED_HOSTS").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'webview',
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

ROOT_URLCONF = 'rateMyProf.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'rateMyProf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
sentry_sdk.init(
    dsn=config.get("api", "SENTRY_DSN"),
    integrations=[DjangoIntegration()]
)

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

SENDGRID_API_KEY = config.get("api", "SENDGRID_KEY")

FACULTY_DEPARTMENT_DICT = {'AE': 'Aerospace Engineering',
                           'AG': 'Agricultural and Food Engineering',
                           'AR': 'Architecture and Regional Planning',
                           'AT': 'Advanced Technology Development Centre',
                           'BM': 'Vinod Gupta School of Management',
                           'BS': 'Bio Science',
                           'BT': 'Biotechnology',
                           'CD': 'Centre for Computational and Data Sciences',
                           'CE': 'Civil Engineering',
                           'CH': 'Chemical Engineering',
                           'CL': 'Centre For Oceans,Rivers,Atmosphere and Land Science',
                           'CR': 'Cryogenic  Engineering',
                           'CS': 'Computer Science and Engineering',
                           'CY': 'Chemistry',
                           'DE': 'Deysarkar Centre of Excellence in Petroleum Engineering',
                           'EC': 'Electronics and Electrical Communication Engg.',
                           'EE': 'Electrical Engineering',
                           'EF': 'Environmental Science and Engineering',
                           'ES': 'Energy Science and Engineering',
                           'ET': 'Centre For Educational Technology',
                           'GG': 'Geology and Geophysics',
                           'GS': 'G.S Sanyal School of Telecommunication',
                           'HS': 'Humanities and Social Sciences',
                           'ID': 'Ranbir and Chitra Gupta School of Infrastructure Design and Mngt.',
                           'IM': 'Industrial and Systems Engineering',
                           'IP': 'Rajiv Gandhi School of Intellectual Property Law',
                           'MA': 'Mathematics',
                           'ME': 'Mechanical Engineering',
                           'MI': 'Mining Engineering',
                           'MM': 'School of Medical Science and Technology',
                           'MS': 'Materials Science Centre',
                           'MT': 'Metallurgical and Materials Engineering',
                           'NA': 'Ocean Engg and Naval Architecture',
                           'PH': 'Physics',
                           'RD': 'Rural Development',
                           'RE': 'Subir Chowdhury School of Quality and Reliability',
                           'RJ': 'Rajendra Mishra School of Engg Entrepreneurship',
                           'RT': 'Rubber Technology',
                           'RX': 'Rekhi Centre of Excellence for the Science of Happiness',
                           'WM': 'School of Water Resources'}

FACULTY_DEPARTMENT_DICT_REVERSE = {'Advanced Technology Development Centre': 'AT',
                                     'Aerospace Engineering': 'AE',
                                     'Agricultural and Food Engineering': 'AG',
                                     'Architecture and Regional Planning': 'AR',
                                     'Bio Science': 'BS',
                                     'Biotechnology': 'BT',
                                     'Centre For Educational Technology': 'ET',
                                     'Centre For Oceans,Rivers,Atmosphere and Land Science': 'CL',
                                     'Centre for Computational and Data Sciences': 'CD',
                                     'Chemical Engineering': 'CH',
                                     'Chemistry': 'CY',
                                     'Civil Engineering': 'CE',
                                     'Computer Science and Engineering': 'CS',
                                     'Cryogenic  Engineering': 'CR',
                                     'Deysarkar Centre of Excellence in Petroleum Engineering': 'DE',
                                     'Electrical Engineering': 'EE',
                                     'Electronics and Electrical Communication Engg.': 'EC',
                                     'Energy Science and Engineering': 'ES',
                                     'Environmental Science and Engineering': 'EF',
                                     'G.S Sanyal School of Telecommunication': 'GS',
                                     'Geology and Geophysics': 'GG',
                                     'Humanities and Social Sciences': 'HS',
                                     'Industrial and Systems Engineering': 'IM',
                                     'Materials Science Centre': 'MS',
                                     'Mathematics': 'MA',
                                     'Mechanical Engineering': 'ME',
                                     'Metallurgical and Materials Engineering': 'MT',
                                     'Mining Engineering': 'MI',
                                     'Ocean Engg and Naval Architecture': 'NA',
                                     'Physics': 'PH',
                                     'Rajendra Mishra School of Engg Entrepreneurship': 'RJ',
                                     'Rajiv Gandhi School of Intellectual Property Law': 'IP',
                                     'Ranbir and Chitra Gupta School of Infrastructure Design and Mngt.': 'ID',
                                     'Rekhi Centre of Excellence for the Science of Happiness': 'RX',
                                     'Rubber Technology': 'RT',
                                     'Rural Development': 'RD',
                                     'School of Medical Science and Technology': 'MM',
                                     'School of Water Resources': 'WM',
                                     'Subir Chowdhury School of Quality and Reliability': 'RE',
                                     'Vinod Gupta School of Management': 'BM'}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOGOUT_REDIRECT_URL = "index"

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
