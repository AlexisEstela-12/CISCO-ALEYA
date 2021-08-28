from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Devices_Historial


class Formulario(ModelForm):

    guia_devolucion = forms.ImageField() 
    # descripcion = forms.CharField(label="Informacion Extra")

    class Meta :
        model = Devices_Historial
        fields = ('identificador','serial_number','modelo','AM','partner','responsable','cliente','contacto','Fprestamo','Fentregado','codigo_prestamo','guia_devolucion') 
        