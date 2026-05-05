from django.forms import ModelForm

from proveedores.models import Proveedor

class FormProveedor(ModelForm):

    class Meta:
        model = Proveedor
        fields = ('__all__')
