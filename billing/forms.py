from django import forms
from .models import factura, detalleFacturaProveedor, facturaProveedor
from django.forms import inlineformset_factory

class FacturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = '__all__'

class FacturaProveedorForm(forms.ModelForm):
    class Meta:
        model = facturaProveedor
        fields = ['numero', 'fecha', 'costo_envio', 'proveedor']

class FacturaProveedorDetalleForm(forms.ModelForm):
    class Meta:
        model = detalleFacturaProveedor
        fields = ['producto', 'cantidad', 'precio_unitario', 'descuento']

detalleProveedorFormSet = inlineformset_factory(
    facturaProveedor,
    detalleFacturaProveedor,
    form = FacturaProveedorDetalleForm,
    extra = 3,
    can_delete=True,
)