import json
import os

from dotenv import load_dotenv
from google.cloud import secretmanager
from google.oauth2 import service_account

from .static import *

# load creds and get payload, override with local if .env.local exists
local_env = ".env.local"
if os.path.exists(local_env):
    with open("credentials.json", "r") as f:
        credentials = json.load(f)
        credentials = service_account.Credentials.from_service_account_info(credentials)
        client = secretmanager.SecretManagerServiceClient(credentials=credentials)
    load_dotenv(local_env)
    DEBUG = True
else:
    client = secretmanager.SecretManagerServiceClient()
    load_dotenv()
    DEBUG = False

CACHE_HOSTNAME = os.getenv("CACHE_HOSTNAME")
CACHE_USERNAME = os.getenv("CACHE_USERNAME")
CACHE_PORT = os.getenv("CACHE_PORT")
CACHE_VERSION = os.getenv("CACHE_VERSION")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_SECRET_1_ID = os.getenv("GCP_SECRET_1_ID")
GCP_SECRET_2_ID = os.getenv("GCP_SECRET_2_ID")
GCP_VERSION_ID = os.getenv("GCP_VERSION_ID")
FRONTEND_URL = os.getenv("FRONTEND_URL")
BACKEND_URL = os.getenv("BACKEND_URL")

name = f"projects/{GCP_PROJECT_ID}/secrets/{GCP_SECRET_1_ID}/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload = response.payload.data.decode("UTF-8")
name = f"projects/{GCP_PROJECT_ID}/secrets/{GCP_SECRET_2_ID}/versions/{GCP_VERSION_ID}"
response = client.access_secret_version(name=name)
secret_payload_2 = response.payload.data.decode("UTF-8")

ALLOWED_HOSTS = [CACHE_HOSTNAME, DB_HOSTNAME, FRONTEND_URL, BACKEND_URL]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{CACHE_HOSTNAME}:{CACHE_PORT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "USERNAME": CACHE_USERNAME,
            "VERSION": CACHE_VERSION,
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
