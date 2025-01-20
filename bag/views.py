from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Inventory

# Create your views here.

def view_shopping_bag(request):
    """ View to return the shopping bag """

    return render (request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of an item to the shopping bag 
        - Code from Boutique Ado with adaptations """

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


def adjust_shopping_bag(request, item_id):
    """ Adjust item quantity in the shopping bag 
        - Code from Boutique Ado with adaptations """
    
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Retrieve current quantity in the shopping bag
    current_quantity = 0
    if size:
        current_quantity = bag.get(item_id, {}).get('items_by_size', {}).get(size, 0)
    else:
        current_quantity = bag.get(item_id, 0)

    if size:
        if quantity > 0:
            # Update inventory if increasing quantity
            inventory_item = Inventory.objects.get(product_id=item_id, size=size)
            if quantity > current_quantity:
                if inventory_item.quantity >= (quantity - current_quantity):
                    inventory_item.quantity -= (quantity - current_quantity)  # Deduct the difference
                    inventory_item.save()
                else:
                    messages.error(request, "Not enough stock available.")
                    return redirect(reverse('view_shopping_bag'))
            elif quantity < current_quantity:
                inventory_item.quantity += (current_quantity - quantity)  # Restore the difference
                inventory_item.save()
            
            # Update the bag quantity
            bag[item_id]['items_by_size'][size] = quantity
        else:
            # Remove item and return stock to inventory
            inventory_item = Inventory.objects.get(product_id=item_id, size=size)
            inventory_item.quantity += current_quantity  # Return the entire quantity to inventory
            inventory_item.save()
            
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            # Update inventory if increasing quantity
            inventory_item = Inventory.objects.get(product_id=item_id)
            if quantity > current_quantity:
                if inventory_item.quantity >= (quantity - current_quantity):
                    inventory_item.quantity -= (quantity - current_quantity)  # Deduct the difference
                    inventory_item.save()
                else:
                    messages.error(request, "Not enough stock available.")
                    return redirect(reverse('view_shopping_bag'))
            elif quantity < current_quantity:
                inventory_item.quantity += (current_quantity - quantity)  # Restore the difference
                inventory_item.save()
            
            # Update the bag quantity
            bag[item_id] = quantity
        else:
            # Remove item and return stock to inventory
            inventory_item = Inventory.objects.get(product_id=item_id)
            inventory_item.quantity += current_quantity  # Return the entire quantity to inventory
            inventory_item.save()
            
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """ Remove item quantity from the shopping bag and update inventory """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            current_quantity = bag.get(item_id, {}).get('items_by_size', {}).get(size, 0)
            if current_quantity > 0:
                # Update inventory to add back the removed quantity
                inventory_item = Inventory.objects.get(product_id=item_id, size=size)
                inventory_item.quantity += current_quantity
                inventory_item.save()

            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            current_quantity = bag.get(item_id, 0)
            if current_quantity > 0:
                # Update inventory to add back the removed quantity
                inventory_item = Inventory.objects.get(product_id=item_id)
                inventory_item.quantity += current_quantity
                inventory_item.save()

            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
