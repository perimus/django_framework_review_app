# Create your views here.

from django.http import request
from django.shortcuts import render

from .forms import ExampleForm


def form_example(request: request) -> render:
    form = ExampleForm()
    for name in request.POST:
        print(f"{name}: {request.POST.getlist(name)}")
    return render(request, "form-example.html", {"method": request.method, "form": form})
