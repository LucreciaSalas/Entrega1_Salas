from django.db import models

# Create your models here.

class Pacientes(models.Model): 
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    dni= models.IntegerField()
    patologia= models.CharField(max_length=40) # ver #
    talla= models.IntegerField()
    peso= models.IntegerField()
    contorno= models.IntegerField() # se espera que ingrese contorno cintura #

class Prestadores(models.Model):
    nombre= models.CharField(max_length=40)
    especialidad= models.CharField(max_length=40)
           
class Proveedores(models.Model):
    nombre= models.CharField(max_length=40)
    cuit= models.IntegerField()
    cbu= models.IntegerField()
   