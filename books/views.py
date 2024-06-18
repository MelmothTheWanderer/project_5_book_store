from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book, Genre
from django.db.models import Q
from django.urls import reverse
from django.db.models.functions import Lower


# Create your views here.

def all_books(request):
    """ A view to display all of the books """

    books = Book.objects.all()
    query = None
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        books = books.filter(genre__caption__in=categories)
        categories = Genre.objects.filter(caption__in=categories)


    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

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
        'current_categories': categories,
    }
    
    return render(request, 'books/books.html', context)

def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
   
    }

    return render(request, 'books/book-details.html', context)

