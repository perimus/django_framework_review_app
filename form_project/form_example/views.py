# Create your views here.

from django.shortcuts import render
from django.http import request

def form_example(request: request) -> render:
    return render(request, "form-example.html") 