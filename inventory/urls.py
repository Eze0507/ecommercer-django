from django.urls import path
from . import views, views_movimiento, views_producto, views_inventario
urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:codigo>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:codigo>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    path('productos/', views_producto.lista_producto, name='lista_producto' ),
    path('productos/nuevo', views_producto.crear_producto, name='crear_producto'),
    path('productos/editar/<int:codigo>/', views_producto.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:codigo>/', views_producto.eliminar_producto, name='eliminar_producto'),

    path('movimientos/', views_movimiento.lista_movimiento, name='lista_movimiento'),
    path('movimientos/nuevo', views_movimiento.crear_movimiento, name='crear_movimiento'),
    path('movimientos/editar/<int:codigo>/', views_movimiento.editar_movimiento, name='editar_movimiento'),
    path('movimientos/eliminar/<int:codigo>/', views_movimiento.eliminar_movimiento, name='eliminar_movimiento'),
    
    path('inventarios/', views_inventario.lista_inventario, name='lista_inventario'),
    path('inventarios/nuevo', views_inventario.crear_inventario, name='crear_inventario'),
    path('inventarios/editar/<int:codigo>/', views_inventario.editar_inventario, name='editar_inventario'),
    path('inventarios/eliminar/<int:codigo>/', views_inventario.eliminar_inventario, name='eliminar_inventario'),
]