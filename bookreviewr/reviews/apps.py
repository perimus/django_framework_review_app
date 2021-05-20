from django.apps import AppConfig
from django.contrib.admin.apps import SimpleAdminConfig


class ReviewsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "reviews"


class ReviewsAdminConfig(SimpleAdminConfig):
    default_site: str = "bookreviewr.admin.BookreviewrAdminSite"
