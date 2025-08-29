from django.db import models
from inventory.models import producto
from customers.models import cliente
from billing.models import factura

# Create your models here.
class carrito(models.Model):
    codigo = models.AutoField(primary_key=True)
    estado = models.BooleanField(default=False)
    cliente = models.OneToOneField(cliente, on_delete=models.CASCADE, related_name='cliente_carrito')

class detalleCarrito(models.Model):
    codigo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='productos_carrito')
    carrito =  models.ForeignKey(carrito, on_delete=models.CASCADE, related_name='carrito')

class pedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    direccion = models.CharField(max_length=100)
    estado = models.CharField(10)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name='cliente_pedidos')
    factura = models.OneToOneField(factura, on_delete=models.CASCADE, related_name='factura_pedido')
