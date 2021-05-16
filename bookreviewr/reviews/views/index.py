from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> render:
    app_name: str = "Bookreviewr"
    return render(request, "base.html", {"app_name": app_name})
