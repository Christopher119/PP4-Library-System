from django.db import models
from django.contrib.auth.models import User

# constant to determine whether there are any remaining books to be reserved by users
STATUS = ((0, "Unavailable"), (1, "Available"))
APPROVAL = ((0, "Awaiting Moderation"), (1, "Approved"))

# Create your models here.

class Book(models.Model):
    """A Model for each Book entry in the database."""
    # name of book
    title = models.CharField(max_length=200, unique=True)
    # url style for name of book
    slug = models.SlugField(max_length=200, unique=True)
    # author of book
    author = models.CharField(max_length=200)
    # genre of book
    genre = models.CharField(max_length=200)
    # blurb for the book
    blurb = models.CharField(max_length=200, unique=True)
    # description of the book
    description = models.TextField(unique=True)
    # number available for check out
    copies_available = models.IntegerField()

    # attribute to set books as available by default
    status = models.IntegerField(choices=STATUS, default=1)

class Review(models.Model):
    """A Model for each Review in the database."""
    # attribute to get the user who left the review
    # also deletes all reviews by user when user is deleted
    reader = models.ForeignKey(
                                User, on_delete=models.CASCADE, 
                                related_name="reviewer"
                                )
    # attribute to get the book the user is reviewing
    # also deletes all reviews on the book if it is deleted                        
    reviewed_book = models.ForeignKey(
                                Book, on_delete=models.CASCADE, 
                                related_name="reviews"
                                )
    # description of the book
    # not unique as some users may leave similar reviews
    review_content = models.TextField()
    # attribute to set review as unavailable by default
    approved = models.IntegerField(choices=APPROVAL, default=0)