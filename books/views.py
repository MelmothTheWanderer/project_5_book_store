from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from django.db.models import Q
from django.urls import reverse


# Create your views here.

def all_books(request):
    """ A view to display all of the books """

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter valid search criteria")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(blurb__icontains=query)
            books = books.filter(queries)

    context = {
        'books' : books,
        'search_term': query,
    }
    
    return render(request, 'books/books.html', context)

def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
   
    }

    return render(request, 'books/book-details.html', context)

