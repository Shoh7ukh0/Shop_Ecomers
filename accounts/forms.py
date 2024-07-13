from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                    'placeholder': 'Username'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'account-inner-form form-control',
                    'placeholder': 'First Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                    'placeholder': 'First name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'account-inner-form form-control',
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'photo', 'country', 'city', 'post_code', 'phone_number']

        widgets = {
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Address'
                }
            ),
            'country': forms.Select(
                attrs={
                    'class': 'account-inner-form form-control',
                    'placeholder': 'Country'
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'City'
                }
            ),
            'post_code': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Post Code'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone'
                }
            )
        }
