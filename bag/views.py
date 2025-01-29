from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Inventory, Product

# Create your views here.


def view_shopping_bag(request):
    """ View to return the shopping bag """

    return render(request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of an item to the shopping bag
        - Code from Boutique Ado with adaptations """

    product = get_object_or_404(Product, pk=item_id)
    size = request.POST.get('size')  # Get size
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Ensure size is selected and not None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Prevent 'NoneType' error when calling .upper()
    size_display = size.upper() if size else "No size selected"

    bag = request.session.get('bag', {})

    # Logic when size is selected
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size_display} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size_display} {product.name} to your shopping bag!')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size_display} {product.name} to your shopping bag!')

        # Reduce inventory only if size is selected
        try:
            inventory_item = Inventory.objects.get(
                product_id=item_id, size=size)
            if inventory_item.quantity >= quantity:
                inventory_item.quantity -= quantity
                inventory_item.save()
            else:
                messages.error(request, "Not enough stock available.")
                return redirect(redirect_url)

        except Inventory.DoesNotExist:
            messages.error(request, f'No inventory found for size {size_display} of {product.name}.')
            return redirect(redirect_url)

    else:
        # Logic for products with no size selected
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}!')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag!')

        # Reduce inventory for non-sized products
        try:
            inventory_item = Inventory.objects.get(product_id=item_id)  # No size specified
            if inventory_item.quantity >= quantity:
                inventory_item.quantity -= quantity
                inventory_item.save()
            else:
                messages.error(request, "Not enough stock available.")
                return redirect(redirect_url)

        except Inventory.DoesNotExist:
            messages.error(request, f'No inventory found for {product.name}.')
            return redirect(redirect_url)

    # Save the updated bag in the session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    """ Adjust item quantity in the shopping bag
        - Code from Boutique Ado with adaptations """

    product = get_object_or_404(Product,pk=item_id)
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
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            # Remove item and return stock to inventory
            inventory_item = Inventory.objects.get(product_id=item_id, size=size)
            inventory_item.quantity += current_quantity  # Return the entire quantity to inventory
            inventory_item.save()

            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag!')
    else:
        if quantity > 0:
            # Update inventory if increasing quantity
            inventory_item = Inventory.objects.get(product_id=item_id)
            if quantity > current_quantity:
                if inventory_item.quantity >= (quantity - current_quantity):
                    inventory_item.quantity -= (quantity - current_quantity)  # Deduct the difference
                    inventory_item.save()
                else:
                    messages.error(request, f'Not enough stock available.')
                    return redirect(reverse('view_shopping_bag'))
            elif quantity < current_quantity:
                inventory_item.quantity += (current_quantity - quantity)  # Restore the difference
                inventory_item.save()

            # Update the bag quantity
            bag[item_id] = quantity
            messages.success(request, f'Update {product.name} quantity to your {bag[item_id]}!')
        else:
            # Remove item and return stock to inventory
            inventory_item = Inventory.objects.get(product_id=item_id)
            inventory_item.quantity += current_quantity  # Return the entire quantity to inventory
            inventory_item.save()

            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """ Remove item quantity from the shopping bag and update inventory """

    try:
        product = get_object_or_404(Product,pk=item_id)
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
            messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag!')
        else:
            current_quantity = bag.get(item_id, 0)
            if current_quantity > 0:
                # Update inventory to add back the removed quantity
                inventory_item = Inventory.objects.get(product_id=item_id)
                inventory_item.quantity += current_quantity
                inventory_item.save()

            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
