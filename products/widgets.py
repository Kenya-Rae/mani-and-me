from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    """Custom widget to allow multiple file uploads."""
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['multiple'] = True
        super().__init__(attrs)