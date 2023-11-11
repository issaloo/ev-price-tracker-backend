import json
import os

from dotenv import load_dotenv
from google.cloud import secretmanager
from google.oauth2 import service_account

from .base import *

load_dotenv("../.env.local")
CACHE_HOSTNAME = os.getenv("CACHE_HOSTNAME")
CACHE_PORT = os.getenv("CACHE_PORT")
CACHE_VERSION = os.getenv("CACHE_VERSION")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_VERSION_ID = os.getenv("GCP_VERSION_ID")
FRONTEND_URL = os.getenv("FRONTEND_URL")

# load credentials and get payload
with open("credentials.json", "r") as f:
    credentials = json.load(f)
    credentials = service_account.Credentials.from_service_account_info(credentials)
client = secretmanager.SecretManagerServiceClient(credentials=credentials)
name = f"projects/{GCP_PROJECT_ID}/secrets/redis_cache/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload = response.payload.data.decode("UTF-8")
name = f"projects/{GCP_PROJECT_ID}/secrets/postgres_db/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload_2 = response.payload.data.decode("UTF-8")

ALLOWED_HOSTS = [CACHE_HOSTNAME, DB_HOSTNAME, FRONTEND_URL, "ev-price-tracker.uc.r.appspot.com"]
DEBUG = True
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{CACHE_HOSTNAME}:{CACHE_PORT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "VERSION": f"{CACHE_VERSION}",
            "PASSWORD": secret_payload,
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
        },
    }
}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_DATABASE,
        "USER": DB_USERNAME,
        "PASSWORD": secret_payload_2,
        "HOST": DB_HOSTNAME,
        "PORT": DB_PORT,
    }
}