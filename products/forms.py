from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Div
from .models import Product, ProductImage, Category, Inventory
from .widgets import CustomClearableFileInput


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Main Image', required=False,
                             widget=CustomClearableFileInput)
    image_2 = forms.ImageField(label='Additional Image 2', required=False,
                               widget=CustomClearableFileInput)
    image_3 = forms.ImageField(label='Additional Image 3', required=False,
                               widget=CustomClearableFileInput)

    def clean(self):
        cleaned_data = super().clean()
        # Any specific validation for the images
        image_fields = ['image', 'image_2', 'image_3']
        uploaded_images = sum([1 for field in image_fields if cleaned_data.get(field)])

        # Check if the user uploads more than 3 images
        if uploaded_images > 3:
            raise forms.ValidationError(
                'You can only upload a maximum of 3 images.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate the category field with friendly names
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        # Apply crispy form styles
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Product'))

        # Apply custom CSS classes to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-2'


class ProductImageForm(forms.ModelForm):
    # This form will handle both the main image and additional images
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    class Meta:
        model = ProductImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['size', 'quantity']


class InventoryUpdateForm(forms.ModelForm):
    """ Form to update inventory quantities. """
    class Meta:
        model = Inventory
        fields = ['size', 'quantity']

    def __init__(self, *args, **kwargs):
        # Check if we are updating existing inventory; if so, pre-populate the form
        product = kwargs.get('initial', {}).get('product')
        super().__init__(*args, **kwargs)
        if product:
            self.fields['size'].queryset = Inventory.objects.filter(product=product).values_list('size', flat=True).distinct()
            # Set a default value for size if available
            self.fields['quantity'].initial = 1  # Set default quantity to 1


ProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=3, can_delete=True
)
