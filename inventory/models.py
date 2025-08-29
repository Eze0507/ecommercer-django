from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class proveedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    contacto = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.descripcion

class producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="productos/")
    unidad = models.CharField(max_length=5)
    existencia = models.IntegerField()
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_compra_anterior = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class tipoMovimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class inventario(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    fecha = models.DateField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.ForeignKey(tipoMovimiento, on_delete=models.CASCADE, related_name='movimientos')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_inventario', null=True, blank=True)

class detalleInventario(models.Model):
    codigo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    fecha_actualizacion =  models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='productos_inventario')
    inventario = models.ForeignKey(inventario, on_delete=models.CASCADE, related_name='inventarios')