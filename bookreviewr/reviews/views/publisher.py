from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import PublisherForm
from ..models import DBPublisher


def publisher_edit(request: HttpRequest, pk: int = None) -> render:
    """"""

    if pk is not None:
        publisher = get_object_or_404(DBPublisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, f'Publisher "{updated_publisher}" was created.')
            else:
                messages.success(request, f'Publisher "{updated_publisher}" was updated.')

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, "instance-form.html", {"instance": publisher, "model_type": "Publisher", "form": form})
