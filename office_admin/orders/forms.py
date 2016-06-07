from django import forms
from .models import Order

#from django import newforms as forms
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'category']