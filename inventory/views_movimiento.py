from django.shortcuts import render, redirect, get_object_or_404
from .models import tipoMovimiento
from .forms import MovimientoForm

def lista_movimiento(request):
    movimientos = tipoMovimiento.objects.all()
    return render(request, 'movimiento/lista.html', {'movimientos':movimientos})

def crear_movimiento(request):
    form = MovimientoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_movimiento')
    return render(request, 'movimiento/formulario.html', {'form':form})

def editar_movimiento(request, codigo):
    obj = get_object_or_404(tipoMovimiento, codigo=codigo)
    form = MovimientoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('lista_movimiento')
    return render(request, 'movimiento/formulario.html', {'form':form})

def eliminar_movimiento(request, codigo):
    obj = get_object_or_404(tipoMovimiento, codigo=codigo)
    if request.method == 'post':
        obj.delete()
        return redirect('lista_movimiento')
    return render(request, 'movimiento/confirmar.html', {'movimiento':obj})