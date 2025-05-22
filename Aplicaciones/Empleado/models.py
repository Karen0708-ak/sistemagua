from django.db import models

# Create your models here.
class Empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)