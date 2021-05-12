from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    name: str = request.GET.get("name") or "world"
    return HttpResponse(f"Hello, {name}!")
