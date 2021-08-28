from Prestamos.models import Devices
from django.core.mail import EmailMessage
from django.template import Template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def create_mail(user_mail,template_name,context):
    template= get_template(template_name)
    content = template.render(context)
    message = EmailMultiAlternatives(
        subject="Mensaje de aviso de Prestamo",
        body='',
        from_email= settings.EMAIL_HOST_USER,
        to= [
            user_mail
        ],
        cc= ['alestela@cisco.com']
    )

    message.attach_alternative(content,'text/html')
    return message










