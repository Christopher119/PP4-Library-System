from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Review
from .forms import ReviewForm, RequestForm, ReserveForm

# Create your views here.

class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "books/books.html"
    paginate_by = 9

# def book_list(request):
#    model = Book
#    search_request = ""
#    if request.GET.get("searchbar"):
#        search_request = request.GET.get("searchbar")
#    
#    books = Book.objects.filter(title__icontains = search_request)
#    context = {"books": books}
#    paginate_by = 6
#    return render(request, 'books/index1.html')

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
        messages.add_message(
            request, messages.SUCCESS,
            'Review submitted and awaiting approval'
        )

    review_form = ReviewForm()

    return render(
        request,
        "books/book_detail.html",
        {"book": book,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,},
    )

def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.reader == request.user:
            review = review_form.save(commit=False)
            review.reviewed_book = book
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))

def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reader == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))

def request_book(request, request_id):
    """
    view to request a book
    """

    if request.method == "POST":

        request = get_object_or_404(Request, pk=request_id)
        request_form = RequestForm(data=request.POST, instance=request)

        if request_form.is_valid():
            request = request_form.save(commit=False)
            request.save()
            messages.add_message(request, messages.SUCCESS, 'Request Submitted!')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')

    return render(
        request,
        "books/books.html",
        {"book_title": book_title,
        "book_author": book_author,
        "request_content": request_content,
        "request": request,},
    )

# def reserve_book(request, slug):
#     """
#     view to alter available copies of a book
#     """
#     queryset = Book.objects.filter(status=1)
#     book = get_object_or_404(queryset, slug=slug)
#     reserve_form = ReserveForm()
#
#     if book.available_copies >= 0:
#         book.available_copies -= 1
#         messages.add_message(request, messages.SUCCESS, 'Book reserved!')
#     else:
#         messages.add_message(request, messages.ERROR, 'Something went wrong!')
#
#     return HttpResponseRedirect(reverse('book_detail', args=[slug]))