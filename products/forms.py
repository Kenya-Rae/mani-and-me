from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.text import slugify
from .widgets import CustomClearableFileInput
from .models import Product, ProductImage, Inventory, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'border-black rounded-0'

    def save(self, *args, **kwargs):
        # Customize the upload_to path
        # dynamically based on the associated product
        if not self.instance.pk:  # Only for new instances
            product_slug = slugify(self.instance.product.name)
            self.instance.image.field.upload_to = f'product_images/{product_slug}/'
        return super().save(*args, **kwargs)


class InventoryForm(forms.Form):
    size = forms.CharField(required=False)  # For size if has_sizes is True
    quantity = forms.IntegerField(min_value=0, required=True)

    # Add crispy form helper
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'  # optional: Bootstrap class
        self.helper.label_class = 'col-md-4'  # optional
        self.helper.field_class = 'col-md-8'  # optional
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='btn btn-primary'))


# Inline formsets
ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    extra=3,  # Allows adding 3 images by default
    can_delete=True
)


InventoryFormSet = inlineformset_factory(
    Product, Inventory, form=InventoryForm, fields=('size', 'quantity'),
    extra=1, can_delete=True
)
