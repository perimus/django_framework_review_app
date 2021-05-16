from django.http import HttpRequest
from django.shortcuts import render


def search(request: HttpRequest) -> render:
    search_query: str = request.GET.get("search")
    return render(request, "search.html", {"search_query": search_query})