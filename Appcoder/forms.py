from dataclasses import fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Appcoder.models import User





class Cursoformulario(forms.Form):
      nombre = forms.CharField()
      #curso = forms.CharField()
      camada = forms.IntegerField()

class formulariohijo(forms.Form):
      nombre = forms.CharField()
      #curso = forms.CharField()
      camada = forms.IntegerField()     

class UserRegister(UserCreationForm):
      username = forms.CharField()
      email = forms.EmailField()
      password1= forms.CharField()
      password2= forms.CharField()

      last_name = forms.CharField()
      first_name = forms.CharField()

      class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
        help_text = {k:""for k in fields}


class UserEditform(UserCreationForm):
     
      email = forms.EmailField()
      password1= forms.CharField()
      password2= forms.CharField()

      last_name = forms.CharField()
      first_name = forms.CharField()

      class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name','first_name']
        help_text = {k:""for k in fields}

   

class UserEditForm(UserCreationForm):
      username = forms.CharField()
      email=forms.EmailField(label="modificar E-mail")    
      password1:forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
      password2:forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
      
      class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}
