from django.urls import path
from reviews.views import book_detail, books_list

urlpatterns = [
    path("books/", books_list, name="books_list"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
]
