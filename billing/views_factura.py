from django.shortcuts import render, redirect, get_object_or_404
from .models import factura
from .forms import FacturaForm

# Create your views here.

def lista_factura(request):
    facturas = factura.objects.all()
    return render(request, 'factura/lista.html', {'facturas':facturas})

def crear_factura(request):
    form = FacturaForm(request.POST or None)
    if form.is_valid():
        return redirect('lista_factura')
    return render(request, 'factura/formulario.html', {'form':form})

def editar_factura(request, codigo):
    obj = get_object_or_404(factura, codigo=codigo)
    form = FacturaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('lista_factura')
    return render(request, 'factura/formulario.html', {'form':form})

def eliminar_factura(request, codigo):
    obj = get_object_or_404(factura, codigo=codigo)
    if request.method == "POST":
        obj.delete()
        return redirect('lista_factura')
    return render(request, 'factura/confirmar.html', {'factura':obj})