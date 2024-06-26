# forms.py

from django import forms
from .models import Donation, User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'message', ]



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter your email address'
}))
    class Meta:
        model = User

        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']

class CustomSetPasswordForm(SetPasswordForm):
    pass

