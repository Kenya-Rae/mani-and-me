from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory
from .models import Product, Category, Inventory
from .forms import (
    ProductImage, ProductForm, ProductImageFormSet,
    InventoryForm, InventoryUpdateForm
)

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

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
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
    images = product.images.all()

    context = {
        'product': product,
        'images': images,
    }

    return render(request, 'products/product_info.html', context)


@login_required
def add_product(request):
    """ Add a product to the store. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)

        # Check if the product form is valid
        if product_form.is_valid():
            product = product_form.save(commit=False)  # Don't save yet

            # Save the product first (so we can associate images with it)
            product.save()

            # Now, handle additional images (image_2 and image_3)
            image_2 = product_form.cleaned_data.get('image_2')
            image_3 = product_form.cleaned_data.get('image_3')

            # Set image_2 and image_3 to the product instance if present
            if image_2:
                product.image_2 = image_2
            if image_3:
                product.image_3 = image_3

            # Save the product again with the additional images
            product.save()

            # Check if product has sizes
            if product.has_sizes:
                # Define the sizes (you can modify these as needed)
                sizes = ['S', 'M', 'L']  # Example sizes, modify as needed

                # Create inventory items for each size
                for size in sizes:
                    Inventory.objects.create(
                        product=product,
                        size=size,
                        quantity=1  # Default quantity
                    )
                messages.success(request,
                                 'Successfully added product with sizes \
                                     and inventory!')
            else:
                messages.success(request, 'Successfully added product!')

            # Redirect to the products page or wherever you want
            return redirect('products')
        else:
            messages.error(request,
                           'Failed to add product. \
                             Please ensure the form is valid.')

    else:
        product_form = ProductForm()

    return render(request, 'products/add_product.html', {'form': product_form})


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()  # Save the product with any updates

            # Handle additional images if uploaded
            image_2 = form.cleaned_data.get('image_2')
            image_3 = form.cleaned_data.get('image_3')

            if image_2:
                product.image_2 = image_2
            if image_3:
                product.image_3 = image_3

            # Save the product again with the additional images
            product.save()

            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update the product. \
                            Please check the form.')

    else:
        form = ProductForm(instance=product)

    return render(request,
                  'products/edit_product.html',
                  {'form': form, 'product': product})


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
    """ Get all products and inventory information """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    products = Product.objects.prefetch_related('inventory').all()
    return render(request,
                  'products/manage_inventory.html', {'products': products})


@login_required
def update_inventory(request, product_id):
    """ Allows users to update inventory stock for a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)
    inventory = Inventory.objects.filter(product=product)

    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST, initial={'product': product})
        if form.is_valid():
            size = form.cleaned_data.get('size')
            quantity = form.cleaned_data.get('quantity')

            existing_inventory = Inventory.objects.filter(
                product=product, size=size).first()

            if existing_inventory:
                # If size exists, check if the quantity is valid
                if quantity < 0:
                    messages.error(request, "Quantity cannot be negative.")
                else:
                    existing_inventory.quantity = quantity
                    existing_inventory.save()
                    messages.success(request,
                                     f"Updated stock for size {size}.")
            else:
                # Add new size only if it's not already there
                if quantity < 0:
                    messages.error(request, "Quantity cannot be negative.")
                else:
                    Inventory.objects.create(
                        product=product, size=size, quantity=quantity)
                    messages.success(request, f"Added new size {size}.")

            return redirect('manage_inventory')
    else:
        # Pre-fill the form with the current inventory (size and quantity)
        inventory_item = inventory.first() if inventory.exists() else None
        form = InventoryUpdateForm(
            initial={
                'product': product,
                # Default to 'M' if no inventory exists
                'size': inventory_item.size if inventory_item else 'M',
                # Default to 1 if no inventory exists
                'quantity': inventory_item.quantity if inventory_item else 1,
            }
        )

    return render(request,
                  'products/update_inventory.html',
                  {'form': form, 'product': product})
