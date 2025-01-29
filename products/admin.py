from django.contrib import admin
from .models import Product, Category, ProductImage, Inventory

# Admin classes to customise admin view


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class InventoryInline(admin.TabularInline):
    """ Inline for managing product inventory """
    model = Inventory
    extra = 1  # Allow adding inventory entries directly
    fields = ('size', 'quantity')
    readonly_fields = ('size',)  # Keep 'size' non-editable


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'image',
        'rating',
        'has_sizes',
    )
    inlines = [ProductImageInline, InventoryInline]
    ordering = ('sku',)
    list_filter = ('category', 'has_sizes')
    search_fields = ('name', 'sku', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register models with the admin site


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory)
