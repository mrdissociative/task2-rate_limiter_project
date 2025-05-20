from django.apps import AppConfig # type: ignore


class LimiterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'limiter'
