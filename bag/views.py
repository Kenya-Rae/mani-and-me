from django.shortcuts import render, redirect

# Create your views here.

def view_shopping_bag(request):
    """ View to return the shopping bag """

    return render (request, 'bag/shopping_bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of an item to the shopping bag """

    size = request.POST.get('size')  # Get size
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

     # Create a composite key for size and item_id
    item_key = f'{item_id}_{size}'

    if item_id in bag:
        if size in bag[item_id]['sizes']:
            bag[item_id]['sizes'][size] += quantity
        else:
            bag[item_id]['sizes'][size] = quantity
    else:
        bag[item_id] = {'sizes': {size: quantity}}

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