from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, Inventory


def view_shopping_bag(request):
    """ View to return the shopping bag """
    return render(request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Check the inventory for the selected size if applicable
    if size:
        inventory = Inventory.objects.filter(
            product=product, size=size
            ).first()
        if inventory and inventory.quantity < quantity:
            messages.error(request,
                           f"Not enough stock for size \
                             {size.upper()} of {product.name}.")
            return redirect(redirect_url)

    # Check if we have an existing bag, else initialize one
    bag = request.session.get('bag', {})

    # If size is provided, handle the size-specific inventory update
    if size:
        if item_id in bag:
            if size in bag[item_id]['items_by_size']:
                if bag[item_id]['items_by_size'][size] + quantity <= inventory.quantity:
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(request,
                                     f'Updated size {size.upper()} \
                                        {product.name} quantity to \
                                            {bag[item_id]["items_by_size"][size]}')
                else:
                    messages.error(request,
                                   f"Not enough stock for size \
                                    {size.upper()} of {product.name}.")
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'Added size \
                                    {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added size \
                                 {size.upper()} {product.name} to your bag')
    else:
        if item_id in bag:
            if bag[item_id] + quantity <= inventory.quantity:
                bag[item_id] += quantity
                messages.success(request,
                                 f'Updated {product.name} quantity \
                                    to {bag[item_id]}')
            else:
                messages.error(request,
                               f"Not enough stock for {product.name}.")
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    """ Adjust the quantity of the
    specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Handle size-specific logic
    if size:
        inventory = Inventory.objects.filter(
            product=product, size=size
            ).first()
        if inventory and inventory.quantity < quantity:
            messages.error(request,
                           f"Not enough stock for size \
                            {size.upper()} of {product.name}.")
            return redirect(reverse('view_shopping_bag'))

        # Adjust the bag and inventory
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Updated size {size.upper()} {product.name} \
                                quantity to \
                                    {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             f'Removed size \
                                 {size.upper()} {product.name} from your bag')
    else:
        inventory = Inventory.objects.filter(product=product).first()
        if inventory and inventory.quantity < quantity:
            messages.error(request, f"Not enough stock for {product.name}.")
            return redirect(reverse('view_shopping_bag'))

        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             f'Updated {product.name} \
                                 quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        # Check if the item is in the bag
        if size:
            if item_id in bag.keys() and size in bag[item_id]['items_by_size']:
                # Simply remove the item from the bag without updating stock
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)

                messages.success(request,
                                 f'Removed size {size.upper()} {product.name} \
                                     from your bag')
        else:
            if item_id in bag.keys():
                # Simply remove the item from the bag without updating stock
                bag.pop(item_id)
                messages.success(request,
                                 f'Removed {product.name} from your bag')

        # Save the updated bag to session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
