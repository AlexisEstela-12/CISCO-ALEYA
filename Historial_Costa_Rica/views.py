from django.http import request
from Prestamos_Costa_Rica.models import Devices
from django.shortcuts import redirect, render
from Historial_Costa_Rica.models import Devices_Historial
from .forms import Formulario
from Prestamos_Costa_Rica.models import  AM
from django.db.models import Q
# Create your views here.

def historial(request):

    histo = Devices_Historial.objects.all()
    return render (request,"Historial_CR/historial_CR.html",{"histo": histo})


def buscar_historial(request):
    if request.method == "POST":
        busqueda  = request.POST['busqueda']
        objeto = Devices_Historial.objects.filter(Q(identificador__icontains=busqueda)|Q(serial_number__icontains=busqueda)|Q(modelo__icontains=busqueda)|Q(partner__icontains=busqueda)|Q(responsable__icontains=busqueda)|Q(cliente__icontains=busqueda)|Q(codigo_prestamo__icontains=busqueda))
    return render(request,"Historial_CR/busqueda_historial_CR.html",{"busqueda":busqueda,"objeto":objeto})


def agregar (request,equipo_id):

    value = Devices.objects.get(id = equipo_id)
    form_histo = Formulario(instance=value)

    if request.method == "POST":
        form_histo = Formulario(request.POST,request.FILES)
  
        if form_histo.is_valid():
            form_histo.save()
            return redirect("Historial_CR")
    return render (request,"Historial_CR/tabla_CR.html",{"form_histo": form_histo})
    