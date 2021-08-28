from django.forms.widgets import Widget
from .models import Devices
from django import forms
from django.db.models import query
from django.forms import ModelForm, fields, models
from .models import Devices




class Formulario(ModelForm):

    class Meta:
        model = Devices
        # fields = '__all__'
        fields = ('identificador','serial_number','modelo','codigo_prestamo','AM','partner','responsable','cliente','contacto','correo_contacto','Fprestamo','Fentrega','estado') 
