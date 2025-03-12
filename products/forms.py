"""
Form for adding / updating products by store owner
"""
from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Product form with all fields for adding / updating products
    - displays category friendly names in choices dropdown &
    replaces standard file input with a custom clearable file input
    """
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'summary': SummernoteWidget(),
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
