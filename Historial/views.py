from django.http import request
from Prestamos.models import Devices
from django.shortcuts import redirect, render
from Historial.models import Devices_Historial
from .forms import Formulario
from Prestamos.models import Devices, AM
from django.db.models import Q
# Create your views here.

def historial(request):

    histo = Devices_Historial.objects.all()
    return render (request,"Historial/historial.html",{"histo": histo})


def buscar_historial(request):
    if request.method == "POST":
        busqueda  = request.POST['busqueda']
        objeto = Devices_Historial.objects.filter(Q(identificador__icontains=busqueda)|Q(serial_number__icontains=busqueda)|Q(modelo__icontains=busqueda)|Q(partner__icontains=busqueda)|Q(responsable__icontains=busqueda)|Q(cliente__icontains=busqueda)|Q(codigo_prestamo__icontains=busqueda))
    return render(request,"Historial/busqueda_historial.html",{"busqueda":busqueda,"objeto":objeto})


def agregar (request,equipo_id):

    prueba = AM.objects.all()
    value = Devices.objects.get(id = equipo_id)
    form_histo = Formulario(instance=value)

    if request.method == "POST":
        form_histo = Formulario(request.POST,request.FILES)
        if form_histo.is_valid():
            form_histo.save()
            return redirect("Historial")
    return render (request,"Historial/tabla.html",{"form_histo": form_histo})
    





        

    






