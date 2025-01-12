from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]