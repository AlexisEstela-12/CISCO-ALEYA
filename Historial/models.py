from django.db import models
from django.db.models.deletion import CASCADE
from Prestamos.cambiar_nombre_prestamo import path_and_rename
from Prestamos.models import AM




class Devices_Historial (models.Model):
    identificador = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    AM = models.ForeignKey(AM,on_delete=CASCADE)
    partner = models.CharField(max_length=50)
    responsable = models.CharField(max_length=25)
    cliente = models.CharField(max_length=50)
    contacto = models.CharField(max_length=30)
    correo_contacto = models.EmailField(max_length=40)
    Fprestamo = models.DateTimeField()
    Fentregado = models.DateTimeField()
    codigo_prestamo = models.IntegerField()
    guia_devolucion = models.ImageField(upload_to=path_and_rename, blank= True , null = True)


    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.modelo


