from .models import Review, Request
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_content',)


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('book_author', 'book_author', 'request_content',)