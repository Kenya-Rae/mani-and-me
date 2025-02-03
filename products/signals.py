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
        Inventory.objects.create(product=instance, size=None, quantity=1)  # Default stock = 1


# @receiver(post_save, sender=Inventory)
# def notify_admin_on_low_stock(sender, instance, **kwargs):
#     """ Notify admin when stock is low """
#     if instance.quantity <= 5:
#         send_mail(
#             subject=f"Low Stock Alert: {instance.product.name} ({instance.size})",
#             message=f"Stock for {instance.product.name} (Size: {instance.size}) is low. Only {instance.quantity} left.",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.ADMIN_EMAIL],
#         )
