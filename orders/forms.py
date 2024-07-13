from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
        postal_code = USZipCodeField()
        class Meta:
                model = Order
                fields = ['first_name', 'last_name', 'email', 'address',
                        'postal_code', 'city']
                
                widgets = {
                        'first_name': forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'rows': 2,
                                        'placeholder': 'First Name'
                                }),
                        'last_name': forms.TextInput(
                                attrs={
                                        'class': 'account-inner-form form-control',
                                        'placeholder': "Last Name"
                                }),
                        'email': forms.EmailInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder': "Email"
                                }),
                        'address': forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder': "Address"
                                }),
                        'postal_code': forms.EmailInput(
                                attrs={
                                        'class': 'form-control',
                                        'value': "123456"
                                }),
                        'city': forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder': "City"
                                }),
                }

                