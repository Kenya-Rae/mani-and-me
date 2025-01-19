from django import template

register = template.Library()

@register.filter
def get_friendly_names(categories):
    """
    A custom template filter that returns the friendly names of categories as a comma-separated string.
    """
    return ", ".join(category.friendly_name for category in categories)