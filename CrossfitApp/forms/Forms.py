from django.forms import ModelForm
from ..models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CompetitionEnrollForm(ModelForm):
  
    class Meta:
        model = Competitors
        fields = ['competition_in', 'name', 'lastname', 'age', 'avatar', 'user_linked' ]
        labels = {
           'competition_in' : 'Competicion a inscribirse',
           'name' : 'Nombre', 
           'lastname': 'Apellido', 
           'age':'Edad', 
           'avatar': 'Imagen', 
           'user_linked':"Usuario relacionado: NO MODIFICAR"
        }
        

class ReviewsBlogsForm(ModelForm): 
    class Meta: 
        model = Review
        fields = "__all__"
        labels = {
           'name' : 'Nombre',
           'text' : 'Contenido', 
           'Category': 'Categoria'
        }


class CreateCompetition(ModelForm): 
    class Meta:
        model = Competition
        fields = '__all__'
        labels = {
           'name' : 'Nombre',
           'state' : 'Estado', 
           'country': 'Pais',
           'category': 'Categoria' 
        }

class UserEditForm(forms.Form): 
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="last Name")
    username = forms.CharField(label="Username")

    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}
        exclude = ["password"]