from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ View to show products, including filtering and queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render (request, 'products/products.html', context)


def product_info(request, product_id):
    """ View to show product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render (request, 'products/product_info.html', context)