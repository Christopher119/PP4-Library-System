from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book

# Create your views here.

class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "books/index1.html"
    paginate_by = 6

def home(request): 
    return render(request, "books/index.html") 

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

    reviews = book.reviews.all()
    review_count = book.reviews.filter(approved=True).count()

    return render(
        request,
        "books/book_detail.html",
        {"book": book,
        "reviews": reviews,
        "review_count": review_count,},
        
    )