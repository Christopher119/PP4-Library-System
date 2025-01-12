from django.db import models
from django.contrib.auth.models import User

# constant to determine whether there are any remaining books to be reserved by users
STATUS = ((0, "Unavailable"), (1, "Available"))

# Create your models here.

class Book(models.Model):
    """A Model for each Book entry in the database."""
    # name of book
    title = models.CharField(max_length=200, unique=True)
    # url style for name of book
    slug = models.SlugField(max_length=200, unique=True)
    # author of book
    author = models.SlugField(max_length=200, unique=True)
    # genre of book
    genre = models.SlugField(max_length=200, unique=True)
    # blurb for the book
    blurb = models.SlugField(max_length=200, unique=True)
    # description of the book
    description = models.SlugField(max_length=200, unique=True)
    # number available for check out
    copies_available = models.SlugField(max_length=200, unique=True)

    # attribute to set books as available by default
    status = models.IntegerField(choices=STATUS, default=1)