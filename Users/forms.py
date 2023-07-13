from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class RegisterForm(UserCreationForm):
    account_types = (
        ('Seller', 'Seller'),
        ('Admin', 'Admin'),
        ('Buyer', 'Buyer'),
    )
    account_type = forms.ChoiceField(choices=account_types)
    
    class Meta:
        model = Account
        fields = ('username', 'email', 'account_type', 'password1', 'password2')
