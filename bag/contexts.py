from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book

def bag_contents(request):


    bag_items = []
    total = 0
    book_count = 0
    bag = request.session.get('bag', {})

    for book_id, quantity in bag.items():
        book = get_object_or_404(Book, pk=book_id)
        total += quantity * book.price
        book_count += quantity
        bag_items.append({
            'book_id':book_id,
            'quantity':quantity,
            'book': book,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context