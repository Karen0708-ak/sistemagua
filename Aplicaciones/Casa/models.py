from django.db import models

# Create your models here.
class Casa(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)
    propietario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
