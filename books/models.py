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

    # metadata that sorts entries in descending order
    # by title, by author, and by genre
    class Meta:
        ordering = ["title", "author", "genre"]

    # Method to display Book objects as user friendly string
    def __str__(self):
        return f"{self.author} | {self.title}"

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
    # not unique as some users may leave similar reviews
    review_content = models.TextField()
    # attribute to set review as unavailable by default
    approved = models.IntegerField(choices=APPROVAL, default=0)

    # metadata that sorts entries in descending order
    # by title, by author, and by genre
    class Meta:
        ordering = ["reader", "reviewed_book"]

    # Method to display Book objects as user friendly string
    def __str__(self):
        return f"Review for: {self.reviewed_book.title} | By: {self.reader}"


class Request(models.Model):
    """A Model for each Request in the database."""

    # attribute to get the user who left the review
    # also deletes all reviews by user when user is deleted
    requester = models.ForeignKey(
                                User, on_delete=models.CASCADE, 
                                related_name="requester"
                                )
    # not unique as many users may request
    book_author = models.CharField()
    book_title = models.CharField()
    #allowing optional request reasons
    request_content = models.CharField(blank=True)


    # metadata that sorts entries by requester
    class Meta:
        ordering = ["requester"]

    # Method to display Book objects as user friendly string
    def __str__(self):
        return f"Request for: Title: {self.book.title} Author: {self.book_author} | By: {self.requester}"