from ast import List
from django.db import models

#from Appcoder.viewsf import cursos

# Create your models here.


class estudiante(models.Model):
      nombre= models.CharField(max_length=30) 
      #curso = models.CharField#(max_length=30)   
      #camada= models.CharField(max_length=30) 
      

class cursomodel (models.Model): 
      nombre= models.CharField(max_length=30)    
      #curso = models.CharField(max_length=30)   
      camada= models.IntegerField()
      
      
      def __str__(self):
           return  f"Nombre:{self.nombre}" " - "  f"Camada:{self.camada}"

class camadamodel (models.Model):
      nombre= models.CharField(max_length=30)
      camada= models.IntegerField()

class User(models.Model):
      username = models.CharField(max_length=30)
      email = models.EmailField(max_length=30) 
      password1 = models.CharField(max_length=30)
      password2 = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
      first_name= models.CharField(max_length=30)


   

#class Avatar(models.Model):
     # user=models.ForeignKey(User, on_delete=models.CASCADE)
      #imagen=models.ImageField(upload_to='avatares',null=True, blank=True)


      



