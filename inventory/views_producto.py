from django.shortcuts import redirect, render, get_object_or_404
from .models import producto
from .forms import ProductoForm

def lista_producto(request):
    productos = producto.objects.all()
    return render(request, 'producto/lista.html', {'productos':productos})

def crear_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_producto')
    return render(request, 'producto/formulario.html', {'form':form})

def editar_producto(request, codigo):
    obj = get_object_or_404(producto, codigo=codigo)
    form = ProductoForm(request.POST or None, request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('lista_producto')
    return render(request, 'producto/formulario.html', {'form':form})

def eliminar_producto(request, codigo):
    obj = get_object_or_404(producto, codigo=codigo)
    if request.method == 'POST':
        obj.delete()
        return redirect('lista_producto')
    return render(request, 'producto/confirmar.html', {'producto':obj})
