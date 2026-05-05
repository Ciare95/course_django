from django.shortcuts import render, redirect, get_object_or_404

from proveedores.models import Proveedor
from proveedores.forms import FormProveedor


URL_PROVEEDORES_LIST = 'proveedor:proveedores_list'

def add_proveedor(request):

    if request.method == 'POST':
        proveedor = FormProveedor(request.POST)
        if proveedor.is_valid():
            proveedor.save()
            return redirect(URL_PROVEEDORES_LIST)
    else:
        proveedor = FormProveedor()
        return render(
            request,
            'proveedores/add_proveedor.html',
            {'proveedor': proveedor}
        )

def show_proveedores(request):

    proveedores = Proveedor.objects.all()
    if request.method == 'GET':
        return render(
            request,
            'proveedores/proveedores_list.html',
            {'proveedores': proveedores}
        )

def update_proveedor(request, id):

    proveedor_get = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        proveedor = FormProveedor(request.POST, instance=proveedor_get)
        if proveedor.is_valid():
            proveedor.save()
            return redirect(URL_PROVEEDORES_LIST)
    else:
        proveedor = FormProveedor(instance=proveedor_get)
        return render(
            request,
            'proveedores/update_proveedor.html',
            {'proveedor': proveedor}
        )

def delete_proveedor(request, id):

    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect(URL_PROVEEDORES_LIST)