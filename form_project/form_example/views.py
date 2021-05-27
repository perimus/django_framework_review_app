# Create your views here.

from django.http import request
from django.shortcuts import render

from .forms import OrderForm

initial = {"email": "user@example.com"}


def form_example(request: request) -> render:
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form = OrderForm(initial=initial)
    return render(request, "form-example.html", {"method": request.method, "form": form})
