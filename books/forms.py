from .models import Book, Review, Request
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_content',)


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('book_title', 'book_author', 'request_content',)


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('copies_available',)