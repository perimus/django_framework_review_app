from django.contrib import admin
from reviews.models import DBBook, DBBookContributor, DBContributor, DBPublisher, DBReview

admin.site.register(DBPublisher)
admin.site.register(DBContributor)
admin.site.register(DBBook)
admin.site.register(DBBookContributor)
admin.site.register(DBReview)
