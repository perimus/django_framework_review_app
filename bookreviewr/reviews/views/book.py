from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from reviews.models import DBBook
from reviews.utils import calc_average_rating


def books_list(request: HttpRequest) -> render:
    """"""

    books = DBBook.objects.all()
    book_list = []

    for book in books:
        reviews = book.dbreview_set.all()
        amount_reviews = 0
        book_rating = None
        if reviews:
            book_rating = calc_average_rating([review.rating for review in reviews])
            amount_reviews = len(reviews)

        book_list.append({"book_info": book, "book_rating": book_rating, "amount_reviews": amount_reviews})

    context = {"book_list": book_list}

    return render(request, "reviews/books_list.html", context)


def book_detail(request: HttpRequest, book_id: int) -> render:
    """"""

    book = get_object_or_404(DBBook, pk=book_id)
    reviews = book.dbreview_set.all()
    book_rating = None
    if reviews:
        book_rating = calc_average_rating([review.rating for review in reviews])

    context = {"book": book, "reviews": reviews, "book_rating": book_rating}

    return render(request, "reviews/book.html", context)
