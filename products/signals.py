from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Inventory


@receiver(post_save, sender=Product)
def create_inventory(sender, instance, created, **kwargs):
    """
    Automatically creates an inventory entry when a new product is added,
    only if the product does not have sizes.
    """
    if created and not instance.has_sizes:
        # Default stock = 1
        Inventory.objects.create(product=instance, size=None, quantity=1)
