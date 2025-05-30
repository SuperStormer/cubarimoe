import os

from cubarimoe.settings.base import *

SESSION_COOKIE_SECURE = True

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["web", "localhost"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "memcached:11211",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "kacubarimoe",
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "postgres",
        "PORT": "",
    }
}