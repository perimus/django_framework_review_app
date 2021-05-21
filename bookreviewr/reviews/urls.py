from django.urls import path
from django.views.generic.base import TemplateView
from reviews.views import book_detail, books_list

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("books/", books_list, name="books_list"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
]
