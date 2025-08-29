from django.db import models
from inventory.models import proveedor
from inventory.models import producto
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
numero_validador = RegexValidator(regex='^\d{5}$', message='el numero debe tener exactamente 5 numeros', code='numero_invalido')

class factura(models.Model):
    codigo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=5, unique=True, blank=False, null=False, validators=[numero_validador])
    fecha = models.DateField(default=timezone.now, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class facturaProveedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=5, unique=True, blank=False, null=False, validators=[numero_validador])
    fecha = models.DateField(default=timezone.now, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE, related_name='facturas_proveedor')

class detalleFactura(models.Model):
    codigo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, validators=[MinValueValidator(0)])
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    factura = models.ForeignKey(factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='detalles_factura')

class detalleFacturaProveedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, validators=[MinValueValidator(0)])
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    factura_proveedor = models.ForeignKey(facturaProveedor, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='detalles_factura_proveedor')
    
    def clean(self):
        if self.descuento > self.cantidad * self.precio_unitario:
            raise ValidationError("El descuento no puede superar el subtotal")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        self.subtotal = self.cantidad * self.precio_unitario
        self.impuesto = self.subtotal * 0.13
        self.total = self.subtotal + self.impuesto - self.descuento
        super().save(*args, **kwargs)
        factura = self.factura_proveedor
        detalles = factura.detalles.all()
        factura.subtotal = sum(d.subtotal for d in detalles)
        factura.impuesto = sum(d.impuesto for d in detalles)
        factura.descuento = sum(d.descuento for d in detalles)
        factura.total = sum(d.total for d in detalles) + factura.costo_envio
        factura.save()