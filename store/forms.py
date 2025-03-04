from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CheckoutForm(forms.ModelForm):
    class Meta:
         model = Order
         fields = ['product', 'quantity', 'customer_name', 'customer_address', 'customer_email']