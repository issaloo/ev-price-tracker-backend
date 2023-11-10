import os

from dotenv import load_dotenv
from google.cloud import secretmanager

from .base import *

load_dotenv()
CACHE_HOSTNAME = os.getenv("CACHE_HOSTNAME")
CACHE_PORT = os.getenv("CACHE_PORT")
CACHE_VERSION = os.getenv("CACHE_VERSION")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_VERSION_ID = os.getenv("GCP_VERSION_ID")
FRONTEND_URL = os.getenv("FRONTEND_URL")

# load credentials and get payload
client = secretmanager.SecretManagerServiceClient()
name = f"projects/{GCP_PROJECT_ID}/secrets/redis_cache/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload = response.payload.data.decode("UTF-8")


ALLOWED_HOSTS = [CACHE_HOSTNAME, FRONTEND_URL]
DEBUG = False
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://default:{secret_payload}{CACHE_HOSTNAME}:{CACHE_PORT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "VERSION": f"{CACHE_VERSION}",
        },
    }
}
