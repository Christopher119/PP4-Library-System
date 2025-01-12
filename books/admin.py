from django.contrib import admin
from .models import Book, Review, Request
from django_summernote.admin import SummernoteModelAdmin

# registering a class of BookAdmin
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'copies_available')
    search_fields = ['title', 'author', 'genre', 'copies_available']
    list_filter = ('status', 'author', 'genre',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Review)
admin.site.register(Request)