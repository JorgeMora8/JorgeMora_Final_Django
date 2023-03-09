from django.contrib.auth.forms import UserCreationForm
from django import forms

# class MyUserCreationForm(UserCreationForm):

#     # username = forms.CharField(label='', widget=forms.TextInput)
#     # email = forms.CharField(label='')
#     # password = forms.CharField(label='', widget=forms.PasswordInput)
#     first_name = forms.CharField(max_length=40)
#     last_name = forms.CharField(max_length=40)
#     email = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class UserRegistrationForm(UserCreationForm): 
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField(label='Email de usuario')
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k: '' for k in fields}


# class UserRegistrationForm(UserCreationForm): 
#     username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

#     class Meta:

#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {k: '' for k in fields}