# Create your views here.

from django.shortcuts import render
from django.http import request

def form_example(request: request) -> render:
    for name in request.POST:
        print(f"{name}: {request.POST.getlist(name)}")
    return render(request, "form-example.html", {"method": request.method}) 