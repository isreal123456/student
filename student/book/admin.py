from django.contrib import admin

from book.models import book, book_types

# Register your models here.
admin.site.register(book)
admin.site.register(book_types)