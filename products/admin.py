from django.contrib import admin
from .models import Product, Category, ProductImage

# Admin classes to customise admin view.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty image inputs to display

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'image',    
        'rating',
    )
    inlines = [ProductImageInline]  # Add the inline for related product images
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)