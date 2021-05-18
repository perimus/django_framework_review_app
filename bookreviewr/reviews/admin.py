from django.contrib.admin import AdminSite
from reviews.models import DBBook, DBBookContributor, DBContributor, DBPublisher, DBReview

class BookreviewrAdminSite(AdminSite):
    title_header: str = "Bookreviewr Admin"
    site_header: str = "Bookreviewr administration"
    index_title: str = "Bookreviewr site admin"

admin_site: BookreviewrAdminSite = BookreviewrAdminSite(name="bookreviewr")

# Registration of Bookreviewr Models
admin_site.register(DBPublisher)
admin_site.register(DBContributor)
admin_site.register(DBBook)
admin_site.register(DBBookContributor)
admin_site.register(DBReview)