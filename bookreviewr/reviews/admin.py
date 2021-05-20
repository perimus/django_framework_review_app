from typing import Dict, List, Tuple

from django.contrib import admin
from reviews.models import DBBook, DBBookContributor, DBContributor, DBPublisher, DBReview


class BookAdmin(admin.ModelAdmin):
    date_hierarchy: str = "publication_date"
    search_fields: List[str] = ("title", "isbn__exact", "publisher__name__startswith")
    list_display: List[str] = ("title", "isbn")
    list_filter: List[str] = ("publisher", "publication_date")


class ReviewAdmin(admin.ModelAdmin):
    fieldsets: List[Tuple[str, Dict[str, str]]] = (
        (None, {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content", "rating")}),
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display: List[str] = ("first_name", "last_name")
    search_fields: List[str] = ("first_name", "middle_names", "last_name__startswith")
    list_filter: List[str] = ("last_name",)


# Registration of Bookreviewr Models
admin.site.register(DBPublisher)
admin.site.register(DBContributor, ContributorAdmin)
admin.site.register(DBBook, BookAdmin)
admin.site.register(DBBookContributor)
admin.site.register(DBReview, ReviewAdmin)
