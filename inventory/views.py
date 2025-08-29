from django.shortcuts import render, redirect, get_object_or_404
from .models import proveedor
from .forms import ProveedorForm

# Create your views here.
def lista_proveedores(request):
    proveedores = proveedor.objects.all()
    return render(request, 'inventory/lista.html', {'proveedores': proveedores})

def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proveedores')
    return render(request, 'inventory/formulario.html', {'form': form})

def editar_proveedor(request, codigo):
    obj = get_object_or_404(proveedor, codigo=codigo)
    form = ProveedorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('lista_proveedores')
    return render(request, 'inventory/formulario.html', {'form': form})

def eliminar_proveedor(request, codigo):
    obj = get_object_or_404(proveedor, codigo=codigo)
    if request.method == "POST":
        obj.delete()
        return redirect('lista_proveedores')
    return render(request, 'inventory/confirmar.html', {'proveedor': obj})
