from django.contrib import admin


class BookreviewrAdminSite(admin.AdminSite):
    title_header: str = "Bookreviewr Admin"
    site_header: str = "Bookreviewr administration"
    index_title: str = "Bookreviewr site admin"
