from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': "mx-2 my-2 px-2 py-2 rounded-xl"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': "mx-2 my-2 px-2 py-2 rounded-xl"
    }))

class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
   
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': "mx-2 my-2 px-3 py-3 rounded-xl"
        
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email address",
        'class': "mx-2 my-2 px-2 py-2 rounded-xl"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': "mx-2 my-2 px-2 py-2 rounded-xl"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Repeat password",
        'class': "mx-2 my-2 px-2 py-2 rounded-xl"
    }))