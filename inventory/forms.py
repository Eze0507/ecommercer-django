from django import forms
from .models import proveedor, producto, tipoMovimiento, inventario, detalleInventario
from django.forms import inlineformset_factory

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = tipoMovimiento
        fields = '__all__'

class InventarioForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = ['codigo', 'fecha', 'descripcion', 'fecha', 'tipo_movimiento']

class DetalleInventarioForm(forms.ModelForm):
    class Meta:
        model = detalleInventario
        fields = ['producto','cantidad']

DetalleInventarioFormSet = inlineformset_factory(
    inventario,
    detalleInventario,
    form=DetalleInventarioForm,
    extra=3,
    can_delete=True
)