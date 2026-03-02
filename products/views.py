from django.shortcuts import render, redirect, get_object_or_404
from products.form import ProductForm

from products.models import Product

def create_product(request):

    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect('products:show_products')
    else:
        product = ProductForm()

    return render(
        request,
        'products/create_product.html',
        {'product_form': product}
    )

def show_products(request):

    if request.method == 'GET':
        products = Product.objects.all()
        return render(
            request,
            'products/products_list.html',
            {'products': products}
        )

def update_product(request, id):

    get_product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product_new = ProductForm(request.POST, instance=get_product)
        if product_new.is_valid:
            product_new.save()
            return redirect('products:show_products')
    else:
        product = ProductForm(instance=get_product)
        return render(
            request,
            'products/update_product.html',
            {'product': product}
        )

def detail_product(request, id):

    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)
        return render(
            request,
            'products/detail_product.html',
            {'products': product}
        )

def delete_product(request, id):

    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products:show_products')

