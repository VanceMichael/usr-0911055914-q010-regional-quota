SECRET_KEY = "local-only"
DEBUG = False
ROOT_URLCONF = "quota.urls"
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth", "rest_framework"]
MIDDLEWARE = []
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/data/quota.sqlite3"}}
