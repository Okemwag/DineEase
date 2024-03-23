from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'apextech',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

TENANT_MODEL = "tenants.Client"


#AUTH_USER_MODEL = "apps.authentication.CustomUser"



# CELERY

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-result-backend-settings

CELERY_BROKER_URL = RABBITMQ_URL
CELERY_RESULT_BACKEND = "rpc://"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"                               
CELERY_ACCEPT_CONTENT = ["json"]

# CELERY_BEAT_SCHEDULE = {
#     "sync-records": {
#         "task": "apps.core.tasks.sync_records",
#         "schedule": 10.0,
#     },
# }



#RabbitMQ

# RABBITMQ_USER = os.getenv("RABBITMQ_USER", "rabbitmq")
# RABBITMQ_VHOST = ""
# RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
# RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "rabbitmq")
# RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "5672")
# RABBITMQ_DEFAULT_URL = (
#     f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/{RABBITMQ_VHOST}"
# )
# RABBITMQ_URL = os.getenv("RABBITMQ_URL", RABBITMQ_DEFAULT_URL)
#

#Redis

# REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
# REDIS_PORT = os.getenv("REDIS_PORT", "6379")
# REDIS_DB = os.getenv("REDIS_DB", "0")
# REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
# CACHEOPS_REDIS = REDIS_URL
# CACHEOPS_DEFAULTS = {
#     "timeout": 60 * 60
# }
# CACHEOPS = {
#     "auth.user": {"ops": "get", "timeout": 60 * 15},
#     "auth.*": {"ops": ("fetch", "get"), "timeout": 60 * 60},
#     "auth.permission": {"ops": "all", "timeout": 60 * 60},
#     "auth.group": {"ops": "all", "timeout": 60 * 60},
#     "auth.*": {"ops": "all", "timeout": 60 * 60},
#     "auth.*": {"ops": "all", "timeout": 60 * 60},
#     "auth.*": {"ops": "all", "timeout": 60 * 60},



# }


#Flower

# FLOWER_PORT = os.getenv("FLOWER_PORT", "5555")
# FLOWER_URL = f"http://localhost:{FLOWER_PORT}"
# FLOWER_BASIC_AUTH = os.getenv("FLOWER_BASIC_AUTH", "admin:admin")
# FLOWER_URL = f"http://{FLOWER_BASIC_AUTH}@localhost:{FLOWER_PORT}"


#sentry

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
# from sentry_sdk.integrations.celery import CeleryIntegration
# from sentry_sdk.integrations.redis import RedisIntegration
# from sentry_sdk.integrations.rq import RqIntegration
# from sentry_sdk.integrations.logging import LoggingIntegration



# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_DSN"),
#     integrations=[
#         DjangoIntegration(),
#         CeleryIntegration(),
#         RedisIntegration(),
#         RqIntegration(),
#         LoggingIntegration(),
#     ],
#     traces_sample_rate=1.0,

# )


