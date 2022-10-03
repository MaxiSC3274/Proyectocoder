
from django.db import models

# Create your models here.


class Familiar (models.Model):

      nombre= models.CharField(max_length=30)
      apellido= models.CharField(max_length=30)
      Edad = models.CharField(max_length=30)
      Profesion = models.CharField(max_length=30)



