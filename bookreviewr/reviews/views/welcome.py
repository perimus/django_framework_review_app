from django.http import HttpRequest
from django.shortcuts import render
from reviews.models import DBBook

def welcome(request: HttpRequest) -> render:
    """
    """
    return render(request, 'base.html')