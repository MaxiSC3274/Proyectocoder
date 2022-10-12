

from django.db import models

# Create your models here.


class estudiante(models.Model):
      nombre= models.CharField(max_length=30) 
      #curso = models.CharField#(max_length=30)   
      #camada= models.CharField(max_length=30) 
      

class cursomodel (models.Model): 
      nombre= models.CharField(max_length=30)    
      #curso = models.CharField(max_length=30)   
      camada= models.IntegerField()

      def _str_ (self):
           return self.nombre  

class camadamodel (models.Model):
      nombre= models.CharField(max_length=30)
      camada= models.IntegerField()
      
      
   
      



