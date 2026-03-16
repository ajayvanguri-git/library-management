from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('borrow-records/', views.borrow_record_list, name='borrow_records'),
    path('about/', views.about, name='about'),
]