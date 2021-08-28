from Laboratorio.models import Devices_Lab
from django.shortcuts import render,redirect
from Prestamos.models import Devices
from .forms import Formulario
from django.db.models import Q
from django.core.mail import EmailMessage, send_mail
from Laboratorio.views import eliminar
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from Prestamos.models import AM
from Prestamos.plantilla import funcion_Peru
from django.db.models import Q 


# Create your views here.
def funcion_prestar(request):

    prestamo_aux = Devices.objects.all()
    return render (request,"Prestamos/prestamos.html",{"prestamos_aux": prestamo_aux})


def buscar_prestamos(request):
    if request.method == "POST":
        busqueda  = request.POST['busqueda']
        objeto = Devices.objects.filter(Q(identificador__icontains=busqueda)|Q(serial_number__icontains=busqueda)|Q(modelo__icontains=busqueda)|Q(AM__nombre__icontains=busqueda)|Q(partner__icontains=busqueda)|Q(responsable__icontains=busqueda)|Q(cliente__icontains=busqueda)|Q(codigo_prestamo__icontains=busqueda))
    return render(request,"Prestamos/busqueda_prestamo.html",{"busqueda":busqueda,"objeto":objeto})

def create_mail_peru(user_mail,template_name,context,correo):
    template= get_template(template_name)
    content = template.render(context)
    message = EmailMultiAlternatives(
        subject="Mensaje de aviso de Prestamo de ALEYA para PERU",

        body='',
        from_email= settings.EMAIL_HOST_USER,
        to= [
            user_mail
        ],
        cc= ['alestela@cisco.com','julimend@cisco.com','michluna@cisco.com',correo]
    )

    message.attach_alternative(content,'text/html')
    return message

def Nuevo_Prestamo(request,id):

    valor = Devices_Lab.objects.get(id=id)
    form = Formulario(instance = valor)

    if request.method == 'POST':
        form = Formulario(request.POST,request.FILES)
        if form.is_valid():
            temp =  request.POST.get("AM")
            Account_Manager = AM.objects.get(id=temp)
            correo = request.POST.get("correo_contacto")
            partner = request.POST.get("partner")
            cliente = request.POST.get("cliente")
            codigo_prestamo = request.POST.get("codigo_prestamo")
            contacto = request.POST.get("contacto")
            correo_contacto = request.POST.get("correo_contacto")
            fecha_prestamo = request.POST.get("Fprestamo")
            fecha_devolucion = request.POST.get("Fentrega")
            responsable = request.POST.get("responsable")
            context = {
            "valor": valor, 
            "Account_Manager": Account_Manager,
            "codigo_prestamo":codigo_prestamo,
            "cliente":cliente,
            "partner":partner,
            "contacto":contacto,
            "correo_contacto":correo_contacto,
            "fecha_prestamo": fecha_prestamo,
            "fecha_devolucion":fecha_devolucion,
            "responsable":responsable,
            }
            filepath=funcion_Peru(codigo_prestamo,context)
            email = create_mail_peru(correo,"Prestamos/correo.html",context,Account_Manager.email)
            email.attach_file(filepath)
            email.send(fail_silently=False)
            form.save()
            eliminar(request,id)
            return redirect('Prestamos')

    return render(request, 'Prestamos/formulario.html',{"form":form})





