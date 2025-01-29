from django.shortcuts import render
from products.models import Product


def index(request):
    """ View to return homepage and display products """

    products = Product.objects.all().order_by('name')

    return render(request, 'home/index.html', {
        'products': products
    })


def about_us(request):
    return render(request, 'home/about_us.html')


def contact_us(request):
    return render(request, 'home/contact_us.html')
