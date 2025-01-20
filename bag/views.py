from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Inventory

# Create your views here.

def view_shopping_bag(request):
    """ View to return the shopping bag """

    return render (request, 'bag/shopping_bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of an item to the shopping bag """

    size = request.POST.get('size')  # Get size
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

     # Create a composite key for size and item_id
    item_key = f'{item_id}_{size}'

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # Reduce inventory
    inventory_item = Inventory.objects.get(product_id=item_id, size=size)
    if inventory_item.quantity >= quantity:
        inventory_item.quantity -= quantity
        inventory_item.save()
    else:
        messages.error(request, "Not enough stock available.")
        return redirect(redirect_url)

    request.session['bag'] = bag
    return redirect(redirect_url)