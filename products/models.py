from django.db import models


class Category(models.Model):
    """ For frontend categories. 
    Code used from Boutique Ado"""
    class Meta: # Change category name in admin view
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """ For products within the db.
    Code used from Boutique Ado"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) 
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    """ For multiple images per product"""
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

class Inventory(models.Model):
    """ For tracking inventory - Show customers whats available"""
    class Meta: # Change category name in admin view
        verbose_name_plural = 'Inventory'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    size = models.CharField(max_length=10, blank=True, null=True)  # Size field (optional)
    quantity = models.PositiveIntegerField(default=0)  # Inventory count

    def __str__(self):
        if self.size:
            return f"{self.product.name} - Size {self.size}: {self.quantity} in stock"
        return f"{self.product.name}: {self.quantity} in stock"