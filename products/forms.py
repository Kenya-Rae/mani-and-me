from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Div
from .models import Product, ProductImage, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    image = forms.ImageField(label='', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Product'))

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(label='Additional Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = ProductImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # So crispy doesn't wrap it in another <form> tag


# class InventoryForm(forms.ModelForm):
#     class Meta:
#         model = Inventory
#         fields = ['size', 'quantity']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_class = 'form-horizontal'
#         self.helper.label_class = 'col-md-4'
#         self.helper.field_class = 'col-md-8'
#         self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))


ProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=3, can_delete=True
)

# InventoryFormSet = inlineformset_factory(
#     Product, Inventory, form=InventoryForm, extra=1, can_delete=True
# )
