from django.shortcuts import render, redirect, get_object_or_404
from .models import facturaProveedor, detalleFacturaProveedor
from .forms import FacturaProveedorForm, detalleProveedorFormSet
from django.db import transaction

def lista_factura(request):
    facturas = facturaProveedor.objects.all()
    return render(request, 'factura_proveedor/lista.html', {'facturas':facturas})

def ver_factura(request, codigo):
    factura = get_object_or_404(facturaProveedor, codigo=codigo)
    detalle = factura.detalles.all()
    return render(request, 'factura_proveedor/factura.html', {'factura': factura ,'detalle': detalle})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaProveedorForm(request.POST)
        formSet = detalleProveedorFormSet(request.POST)
        if form.is_valid() and formSet.is_valid():
            with transaction.atomic():
                factura = form.save()
                formSet.instance = factura
                formSet.save()
            return redirect('lista_factura')
    else:
        factura = facturaProveedor()
        form = FacturaProveedorForm(instance=factura)
        formSet = detalleProveedorFormSet(instance=factura)
        return render(request, 'factura_proveedor/formulario.html', {'factura':form, 'detalles':formSet})

def editar_factura(request, codigo):
    obj = get_object_or_404(facturaProveedor, codigo=codigo)
    form = FacturaProveedorForm(request.POST or None, instance=obj)
    formSet = detalleProveedorFormSet(request.POST or None, instance=obj)
    if form.is_valid() and formSet.is_valid():
        factura = form.save()
        formSet.instance = factura
        formSet.save()
        return redirect('lista_factura')
    return render(request, 'factura_proveedor/formulario.html', {'factura':form ,'detalle':formSet})

def eliminar_factura(request, codigo):
    obj = get_object_or_404(facturaProveedor, codigo=codigo)
    if request.method == 'POST':
        obj.delete()
        return redirect('lista_factura')
    return render(request, 'factura_proveedor/confirma.html', {'factura':obj})