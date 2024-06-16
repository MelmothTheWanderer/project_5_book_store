from django.shortcuts import render
from .models import Book

# Create your views here.

def all_books(request):
    """ A view to display all of the books """

    books = Book.objects.all()

    context = {
        'books' : books
    }
    
    return render(request, 'home/index.html', context)

