from django.contrib import admin

# Register your models here.

from .models import Book, Author, Genre

class BookAdmin(admin.ModelAdmin):
    list_filter = ("author",)
    list_display = ("title", "author", "price")

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author)