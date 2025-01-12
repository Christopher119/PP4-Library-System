from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book
from .forms import ReviewForm

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
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.reader = request.user
        review.reviewed_book = book
        review.save()

    review_form = ReviewForm()

    return render(
        request,
        "books/book_detail.html",
        {"book": book,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,},
        
    )