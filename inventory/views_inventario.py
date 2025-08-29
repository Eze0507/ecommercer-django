from django.shortcuts import redirect, render, get_object_or_404
from .models import inventario, detalleInventario
from .forms import InventarioForm, DetalleInventarioForm, DetalleInventarioFormSet
from django.contrib.auth.decorators import login_required

@login_required
def lista_inventario(request):
    inventarios = inventario.objects.all()
    return render(request, 'inventario/lista.html', {'inventarios':inventarios})

@login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        formSet = DetalleInventarioFormSet(request.POST)
        if form.is_valid() and formSet.is_valid():
            inventario_obj = form.save(commit=False)
            inventario_obj.usuario = request.user
            inventario_obj.save()
            formSet.instance = inventario_obj
            formSet.save()
            return redirect('lista_inventario')
    else:
        inventario_obj = inventario()  # 👈 Esto es clave
        form = InventarioForm(instance=inventario_obj)
        formSet = DetalleInventarioFormSet(instance=inventario_obj)  # 👈 Esto genera los formularios extra

    return render(request, 'inventario/formulario.html', {
        'form': form,
        'formSet': formSet
    })


@login_required
def editar_inventario(request, codigo):
    obj = get_object_or_404(inventario, codigo=codigo)
    form = InventarioForm(request.POST or None, instance=obj)
    formSet = DetalleInventarioFormSet(request.POST or None, instance=obj)
    if form.is_valid() and formSet.is_valid():
        inventario_obj = form.save()
        formSet.instance = inventario_obj
        formSet.save()
        return redirect('lista_inventario')
    return render(request, 'inventario/formulario.html', {'form':form , 'formSet':formSet})

@login_required
def eliminar_inventario(request, codigo):
    obj = get_object_or_404(inventario, codigo=codigo)
    if request.method == 'POST':
        obj.delete()
        return redirect('lista_inventario')
    return render(request, 'inventario/confirmar.html', {'inventario':obj})