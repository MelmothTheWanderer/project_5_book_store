from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, book_id):
    """ Add a quantity of the specified book to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if book_id in list(bag.keys()):
        bag[book_id] += quantity
    else:
        bag[book_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)