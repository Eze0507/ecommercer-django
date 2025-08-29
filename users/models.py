from django.db import models
from django.conf import settings

# Create your models here.
class empleado(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    sexo = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_empleado')