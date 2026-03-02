from django.urls import path

from products.views import create_product, show_products, update_product, detail_product, delete_product

app_name = 'products'

urlpatterns = [
    path('create_product/',  create_product, name='create_product'),
    path('show_products/', show_products, name='show_products'),
    path('update_product/<int:id>', update_product, name='update_product'),
    path('detail_product/<int:id>', detail_product, name='detail_product'),
    path('delete_product/<int:id>', delete_product, name='delete_product'),
]