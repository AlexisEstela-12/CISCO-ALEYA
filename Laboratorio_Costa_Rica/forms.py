from django.db.models import fields
from django.forms.models import ModelForm
from .models import Devices_Lab

class Formulario(ModelForm):

    class Meta : 
        model = Devices_Lab
        fields = ('identificador','serial_number','modelo','ubicacion','area','estado')



    
