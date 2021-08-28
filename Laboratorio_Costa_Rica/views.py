from django.shortcuts import render,redirect
from django.db.models import Q 
from Laboratorio_Costa_Rica.models import Devices_Lab
from Prestamos_Costa_Rica.models import Devices
from .forms import Formulario
from Historial_Costa_Rica.views import agregar


# Create your views here.

def Laboratorio(request):
    laboratorio = Devices_Lab.objects.all()

    return render(request,"Laboratorio_CR/laboratorio_CR.html",{"laboratorio": laboratorio})


def buscar(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        objeto = Devices_Lab.objects.filter(Q(serial_number__icontains= busqueda)| Q(identificador__icontains=busqueda)| Q (modelo__icontains = busqueda) | Q(ubicacion__icontains = busqueda)| Q(estado__state__icontains = busqueda) | Q(area__sec__icontains = busqueda)).distinct

    return render(request,"Laboratorio_CR/busqueda_CR.html",{"busqueda":busqueda,"objeto":objeto})


def eliminar (request,equipo_id):

    eliminar_equipo = Devices_Lab.objects.get(id = equipo_id)
    if request.method == "POST" : 
        eliminar_equipo.delete()



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
            return redirect("Laboratorio_CR")
    return render (request,'Laboratorio_CR/devolver_CR.html',{"form_lab":form_lab})




 #       Falta funcion de eliminarrr y agregar de prestamos



