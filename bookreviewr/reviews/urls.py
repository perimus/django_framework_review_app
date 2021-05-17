from django.contrib import admin
from django.urls import path
from reviews.views import books_list, book_detail


urlpatterns = [
    path("books/", books_list, name="books_list"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
]
