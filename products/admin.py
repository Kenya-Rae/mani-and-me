from django.contrib import admin
from .models import Product, Category, ProductImage, Inventory

# Admin classes to customise admin view
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

class InventoryInline(admin.TabularInline):
    """ Inline for managing product inventory """
    model = Inventory
    extra = 1  
    fields = ('size', 'quantity') 
    readonly_fields = ('size',)  

class ProductAdmin(admin.ModelAdmin):
    # Code used from Boutique Ado with slight modification
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'image',    
        'rating',
        'has_sizes',  # Display whether the product has sizes
    )
    inlines = [ProductImageInline, InventoryInline]  # Add inlines for images and inventory
    ordering = ('sku',)
    list_filter = ('category', 'has_sizes')  # Add filter to find products with/without sizes
    search_fields = ('name', 'sku', 'description')  # Enable search by these fields

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register models with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory)
