from socket import fromshare
from django import forms

class Cursoformulario(forms.Form):
      nombre = forms.CharField()
      #curso = forms.CharField()
      camada = forms.IntegerField()

class formulariohijo(forms.Form):
      nombre = forms.CharField()
      #curso = forms.CharField()
      camada = forms.IntegerField()      
