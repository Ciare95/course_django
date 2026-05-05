from django.urls import path
from proveedores.views import add_proveedor, show_proveedores, update_proveedor, delete_proveedor

app_name = 'proveedor'

urlpatterns = [
    path('add_proveedor/', add_proveedor, name='add_proveedor'),
    path('proveedores_list/', show_proveedores, name='proveedores_list'),
    path('update_proveedor/<int:id>/', update_proveedor, name='update_proveedor'),
    path('delete_proveedor/<int:id>/', delete_proveedor, name='delete_proveedor'),
]