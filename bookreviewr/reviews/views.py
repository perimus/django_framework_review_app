from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> render:
    # name: str = request.GET.get("name") or "world"
    name: str = "world"
    return render(request, "base.html", {"name": name})
