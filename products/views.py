from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.

def all_products(request):
    """ View to show products, including filtering and queries -
    Code used from Boutique Ado """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    view = 'grid'  # Default view

    # Handle (Grid or List) view toggle 
    if 'view' in request.GET:
        view = request.GET['view']

    if request.GET:
        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif sortkey == 'rating':
                sortkey = 'rating'

            # Handle direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handle category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle search query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Determine current sorting state
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'view': view,  # Pass the current view state to the template
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ View to show product information and inventory 
    - Code used from Boutique Ado (Adapted)"""

    product = get_object_or_404(Product, pk=product_id)
    inventory = product.inventory.all()

    context = {
        'product': product,
        'inventory': inventory,
    }

    return render (request, 'products/product_info.html', context)