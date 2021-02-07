from django import forms
from .models import Customer, Item

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_id', 'weight', 'lending_amount', 'remarks','intrest']
