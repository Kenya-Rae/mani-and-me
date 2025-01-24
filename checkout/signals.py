from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, Order
from products.models import Inventory

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()

@receiver(post_save, sender=Order)
def update_inventory_after_purchase(sender, instance, created, **kwargs):
    """Update inventory after an order is placed."""
    if created:  # Only run if the order is newly created
        # Loop through all items in the order
        for item in instance.items.all():  # Assuming Order has a related 'items' field
            # Find the matching inventory item for the product and size
            inventory_item = Inventory.objects.get(product=item.product, size=item.size)
            
            # Subtract the purchased quantity from the inventory
            inventory_item.quantity -= item.quantity
            inventory_item.save()