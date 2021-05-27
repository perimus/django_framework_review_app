# Create your views here.

from django.http import request
from django.shortcuts import render

from .forms import NewsletterSignupForm


def form_example(request: request) -> render:
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form = NewsletterSignupForm()
    return render(request, "form-example.html", {"method": request.method, "form": form})
