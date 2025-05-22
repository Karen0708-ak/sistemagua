from django.db import models
from Aplicaciones.Empleado.models import Empleado
from Aplicaciones.Casa.models import Casa

# Create your models here.
class InstalacionCaptacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)