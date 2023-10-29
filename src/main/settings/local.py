from .base import *

# import json # TODO: remove
# from google.oauth2 import service_account # TODO: remove

# # TODO: remove
# from google.cloud import secretmanager
# with open("credentials.json", "r") as f:
#     credentials = json.load(f)
#     credentials = service_account.Credentials.from_service_account_info(credentials)

# client = secretmanager.SecretManagerServiceClient(credentials=credentials)
# name = f"projects/{project_id}/secrets/redis_cache/versions/1"
# response = client.access_secret_version(name=name)
# secret_payload = response.payload.data.decode('UTF-8')


# TODO: Keep this
ALLOWED_HOSTS = ["127.0.0.1", "evpricetrackercache.fly.dev"]
DEBUG = True
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379",  # TODO: redis locally
        "LOCATION": "redis://default:{PASSWORD}{HOST}:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "VERSION": "1",
        },
    }
}
