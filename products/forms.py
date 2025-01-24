from django import forms
from django.forms.models import inlineformset_factory
from .models import Product, ProductImage, Inventory, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'border-black rounded-0'


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].widget.attrs['class'] = 'border-black rounded-0'
        self.fields['quantity'].widget.attrs['class'] = 'border-black rounded-0'


# Inline formsets
ProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=1, can_delete=True
)

InventoryFormSet = inlineformset_factory(
    Product, Inventory, form=InventoryForm, extra=1, can_delete=True
)
