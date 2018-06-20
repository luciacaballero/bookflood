from django.contrib import admin
from django.urls import path
from bookflood import views

urlpatterns = [
    path('', views.home, name='home'),
    path('person', views.view_person, name='person'),
    path('books', views.BookList.as_view(), name='books'),
    path('books/add', views.BookCreate.as_view(), name='add_book'),
    path('books/<pk>', views.BookDetail.as_view(), name='book_detail')
]
