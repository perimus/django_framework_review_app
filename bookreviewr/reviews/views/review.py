from typing import Optional

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import ReviewForm
from ..models import DBBook, DBReview


def review_edit(request: HttpRequest, book_pk: int, review_pk:int = None) -> render:
    """
    """

    book: DBBook = get_object_or_404(DBBook, pk=book_pk)

    if review_pk is not None:
        review: Optional[DBReview] = get_object_or_404(DBReview, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():

            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                msg_text = f'Review for "{book}" created.'
            else:
                updated_review.date_edited = timezone.now()
                msg_text = f'Review for "{book}" updated.'
            
            updated_review.save()
            messages.success(request, msg_text)

            return redirect("book_detail", book_pk)
    
    else:
        form = ReviewForm(instance=review)
    
    return render(
        request, 
        "instance-form.html", 
        {
            "form": form,
            "instance": review,
            "model_type": "Review",
            "related_instance": book,
            "related_model_type": "Book",
        }
    )



