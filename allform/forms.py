from django import forms
from django.forms import ModelForm
from .models import Product,Customer

class productForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control'}),
		'quantity': forms.TextInput(attrs={'class': 'form-control'}),
		'price': forms.TextInput(attrs={'class': 'form-control'}),
		
		}


class customerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}),
		'phone': forms.TextInput(attrs={'class': 'form-control'}),
		'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'name@gmail.com'}),
		'address': forms.Textarea(attrs={'class': 'form-control'}),
		}
		