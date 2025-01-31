from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory
from .models import Product, Category
from .forms import ProductImage, ProductForm, ProductImageFormSet, ProductImageForm

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
                messages.error(request, "Please enter a search criteria!")
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

    context = {
        'product': product,
    }

    return render (request, 'products/product_info.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        formset = ProductImageFormSet(request.POST, request.FILES)

        if product_form.is_valid() and formset.is_valid():
            product = product_form.save()
            formset.instance = product
            formset.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        product_form = ProductForm()
        formset = ProductImageFormSet()

    context = {
        'product_form': product_form,
        'formset': formset,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    formset_class = inlineformset_factory(
        Product, ProductImage, form=ProductImageForm, extra=3, can_delete=True
    )

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = formset_class(request.POST, request.FILES, instance=product)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        formset = formset_class(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'formset': formset,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def manage_inventory(request):
    """ View to display all products with inventory details. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    products = Product.objects.all()  # Get all products

    context = {
        'products': products,
    }

    return render(request, 'products/manage_inventory.html', context)
