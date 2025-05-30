from cubarimoe.settings.base import *

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
        "USER": "POSTGRES_USER",
        "PASSWORD": "POSTGRES_PASSWORD",
        "HOST": "postgres",
        "PORT": "",
    }
}
