from django.urls import path
from . import views_factura_proveedor

urlpatterns = [
    path('facturaProveedor/', views_factura_proveedor.lista_factura, name='lista_factura_proveedor'),
    path('facturaProveedor/nuevo', views_factura_proveedor.crear_factura, name='crear_factura'),
    path('facturaProveedor/editar/<int:codigo>/', views_factura_proveedor.editar_factura, name='editar_factura'),
    path('facturaProveedor/eliminar/<int:codigo>/', views_factura_proveedor.eliminar_factura, name='eliminar_factura'),
]