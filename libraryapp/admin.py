from django.contrib import admin
from .models import Book, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower_name', 'borrow_date', 'return_date')
    search_fields = ('borrower_name', 'book__title')