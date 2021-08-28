from django import forms
from django.shortcuts import render,redirect
from Laboratorio.models import Devices_Lab
from .forms import Formulario
from django.core.mail import EmailMessage
from django.db.models import Q 
from Prestamos.models import Devices
from Historial.views import agregar

# from Historial.views import agregar



# Create your views here.

def Laboratorio(request):
    laboratorio = Devices_Lab.objects.all()

    return render(request,"Laboratorio/laboratorio.html",{"laboratorio": laboratorio})

def buscar(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        objeto = Devices_Lab.objects.filter(Q(serial_number__icontains= busqueda)| Q(identificador__icontains=busqueda)| Q (modelo__icontains = busqueda) | Q(ubicacion__icontains = busqueda)| Q(estado__state__icontains = busqueda) ).distinct

    return render(request,"Laboratorio/busqueda.html",{"busqueda":busqueda,"objeto":objeto})


def eliminar (request,equipo_id):

    eliminar_equipo = Devices_Lab.objects.get(id = equipo_id)
    if request.method == "POST" : 
        eliminar_equipo.delete()




def eliminar_prestamo(id):
    eliminar = Devices.objects.get(id=id)
    eliminar.delete()



def agregar_elemento (request,equipo_id):

    agregar_equipo = Devices.objects.get(id = equipo_id)
    form_lab = Formulario(instance=agregar_equipo)

    if request.method == "POST":
        form_lab = Formulario(request.POST)
        if form_lab.is_valid():
            form_lab.save()
            agregar(request,equipo_id)
            eliminar_prestamo(equipo_id)
            return redirect("Laboratorio")
    return render (request,'Laboratorio/devolver.html',{"form_lab":form_lab})



    


