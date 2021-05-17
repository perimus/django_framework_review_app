from django.contrib import admin
from django.urls import path
from reviews.views import welcome, search

urlpatterns = [
    path("", welcome, name=welcome_view),
    path("book-search/", search),
]
