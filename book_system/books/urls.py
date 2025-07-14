from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/', views.create_book, name='create_book'),
    path('<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
]