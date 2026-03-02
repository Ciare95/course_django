from django import forms

from clients.models import Client

class FormClient(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'