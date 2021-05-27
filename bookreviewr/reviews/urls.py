from django.urls import path
from django.views.generic.base import TemplateView
from reviews.views import book_detail, book_search, books_list, publisher_edit

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("books/", books_list, name="books_list"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
    path("book-search/", book_search, name="book_search"),
    path("publishers/<int:pk>/", publisher_edit, name="publisher_edit"),
    path("publishers/new/", publisher_edit, name="publisher_create"),
]
