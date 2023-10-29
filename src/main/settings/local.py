import json
import os

from dotenv import load_dotenv
from google.cloud import secretmanager
from google.oauth2 import service_account

from .base import *

load_dotenv()
CACHE_HOSTNAME = os.getenv("CACHE_HOSTNAME")
CACHE_PORT = os.getenv("CACHE_PORT")
CACHE_VERSION = os.getenv("CACHE_VERSION")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_VERSION_ID = os.getenv("GCP_VERSION_ID")

# load credentials and get payload
with open("credentials.json", "r") as f:
    credentials = json.load(f)
    credentials = service_account.Credentials.from_service_account_info(credentials)
client = secretmanager.SecretManagerServiceClient(credentials=credentials)
name = f"projects/{GCP_PROJECT_ID}/secrets/redis_cache/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload = response.payload.data.decode("UTF-8")

ALLOWED_HOSTS = ["127.0.0.1", "" # TODO: add frontend]
DEBUG = True
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://127.0.0.1:{CACHE_PORT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "VERSION": "1",
            "PASSWORD": secret_payload,
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
        },
    }
}
