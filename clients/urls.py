from django.urls import path
from clients.views import add_client, clients_list, update_client, delete_client

app_name = 'clients'

urlpatterns = [
    path('add_client/', add_client, name='add_name'),
    path('client_list/', clients_list, name='clients_list'),
    path('update_client/<int:id>/', update_client, name='update_client'),
    path('delete_client/<int:id>/', delete_client, name='delete_client'),
]