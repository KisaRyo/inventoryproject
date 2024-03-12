from django import forms
from django.forms import formset_factory
from .models import Product, Orders


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'specifications', 'category', 'quantity', 'status']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['date', 'time']
        widgets = {
            'date':forms.widgets.DateInput(attrs={'type':'date'}),
            'time':forms.widgets.TimeInput(attrs={'type':'time'}),
        }
