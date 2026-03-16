from django.shortcuts import render, get_object_or_404
from .models import Book, BorrowRecord

def home(request):
    books = Book.objects.all()[:5]
    return render(request, 'home.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def borrow_record_list(request):
    records = BorrowRecord.objects.all()
    return render(request, 'borrow_record.html', {'records': records})

def about(request):
    return render(request, 'about.html')