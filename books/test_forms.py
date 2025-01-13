from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({'review_content': 'This is a great post'})
        self.assertTrue(review_form.is_valid())