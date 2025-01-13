from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books/request-book/<int:request_id>',
          views.request_book, name='request'),
    #path('books/', views.book_list, name='books'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]