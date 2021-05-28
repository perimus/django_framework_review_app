from django.urls import path
from django.views.generic.base import TemplateView
from reviews.views import book_detail, book_search, books_list, publisher_edit, review_edit

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    ### Book URL's
    path("books/", books_list, name="books_list"),
    path("books/<int:pk>/", book_detail, name="book_detail"),
    path("book-search/", book_search, name="book_search"),
    ### Publisher URL's
    path("publishers/<int:pk>/", publisher_edit, name="publisher_edit"),
    path("publishers/new/", publisher_edit, name="publisher_create"),
    ### Review URL's
    path("books/<int:book_pk>/reviews/new", review_edit, name="review_create"),
    path("books/<int:book_pk>/reviews/<int:review_pk>", review_edit, name="review_edit"),
]
