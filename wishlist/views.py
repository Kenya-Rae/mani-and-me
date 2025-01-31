from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist

# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    """ Add product to the wishlist """
    product = get_object_or_404(Product, pk=product_id)
    if Wishlist.objects.filter(user=request.user, product=product).exists():
        messages.info(request, f"{product.name} is already in your wishlist.")
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, f"{product.name} added to your wishlist.")
    return redirect('product_info', product_id=product.id)


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove product from the wishlist """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()
    
    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"{product.name} removed from your wishlist.")
    else:
        messages.error(request, f"{product.name} not found in your wishlist.")
        
    return redirect('products')


@login_required
def view_wishlist(request):
    """ View the user's wishlist """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist/wishlist.html', context)