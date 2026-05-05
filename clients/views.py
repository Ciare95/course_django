from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from clients.models import Client
from clients.form import FormClient

APP_REDIRECT = 'clients:clients_list'

def add_client(request):

    if request.method == 'POST':
        client = FormClient(request.POST)
        if client.is_valid():
            client.save()
            return redirect(APP_REDIRECT)
    else:
        client = FormClient()
        return render(
            request,
            'clients/add_client.html',
            {'clients': client}
        )

def clients_list(request):

    if request.method == 'GET':
        clients = Client.objects.all()
        return render(
            request,
            'clients/clients_list.html',
            {'clients': clients}
        )

def update_client(request, id):

    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client = FormClient(request.POST, instance=client)
        if client.is_valid():
            client.save()
            return redirect(APP_REDIRECT)
    else:
        client = FormClient(instance=client)
        return render(
            request,
            'clients/update_client.html',
            {'client': client}
        )

def delete_client(request, id):

    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect(APP_REDIRECT)

