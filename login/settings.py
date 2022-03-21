"""Settings for dev environment."""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lu3+xlyjj940k46e!h$wp#_l5^g4eb4zr(*a286=o6!@di8cbg'

BASE_URL = 'http://localhost:8000'
STATIC_BASE_URL = BASE_URL
SSO_BAD_CERT = False
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Urls of admins
ADMIN_URLS = ['library@iitb.ac.in']

# SSO Config
SSO_TOKEN_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
SSO_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,profile_picture,sex,username,email,program,contacts,insti_address,secondary_emails,mobile,roll_number'
SSO_CLIENT_ID = 'SITIaFUbY6basHIBQUxPCCt35ZXxD3zkqlOQM5Nz'
SSO_CLIENT_ID_SECRET_BASE64 = 'U0lUSWFGVWJZNmJhc0hJQlFVeFBDQ3QzNVpYeEQzemtxbE9RTTVOejphRVdVZFlnUVFBYlZKN1psV0E5Mk1Oc2JKQXZJSmFnSXRKRG5uMzNEY3JYSnZGYm5pczFBUjlPZnNzYW40UTlScWRSVTRZZmhKZWZ4ZnVTMG5peXhtVUVIdE5pN09halpXdWxXcExjRzJyUGI0WGFFRm0zSFFzYTRkRU96TlJDNA=='

# Password Login
SSO_DEFAULT_REDIR = 'https://insti.app/login'
SSO_LOGIN_URL = 'https://gymkhana.iitb.ac.in/sso/account/login/?next=/sso/oauth/authorize/%3Fclient_id%3DSITIaFUbY6basHIBQUxPCCt35ZXxD3zkqlOQM5Nz%26response_type%3Dcode%26scope%3Dbasic%2520profile%2520picture%2520sex%2520ldap%2520phone%2520insti_address%2520program%2520secondary_emails%26redirect_uri%3D' + SSO_DEFAULT_REDIR

MEDIA_ROOT = './upload/static/upload'
MEDIA_URL = 'http://localhost:8000/static/upload/'

USER_AVATAR_URL = '/static/upload/useravatar.jpg'

VAPID_PRIV_KEY = ""
FCM_SERVER_KEY = ""

ROOT_URLCONF = "login.urls"
# Change this to LOGGING to enable SQLite logging
NO_LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
   'login',
   'requirements'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str('/templates')],
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

CORS_ORIGIN_ALLOW_ALL=True
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# EMAIL settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = ''
EMAIL_USE_TLS = True