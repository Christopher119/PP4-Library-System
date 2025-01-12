from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book

# Create your views here.

class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "books/index.html"
    paginate_by = 6

def book_detail(request, slug):
    """
    Display an individual :model:`books.Book`.

    **Context**

    ``book``
        An instance of :model:`books.Book`.

    **Template:**

    :template:`blog/book_detail.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "books/book_detail.html",
        {"book": book},
    )