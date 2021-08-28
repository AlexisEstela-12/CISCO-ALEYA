from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.shortcuts import redirect
from Prestamos.cambiar_nombre_prestamo import path_and_rename


# Create your models here.


class AM (models.Model): 
    nombre = models.CharField(max_length=50)
    telf = models.CharField(max_length= 15)
    email = models.EmailField()

    class Meta:
        verbose_name = "Acount Manager"
        verbose_name_plural = "Acount Managers"

    def __str__(self):
        return self.nombre


class estado(models.Model):
    state=models.CharField(max_length=15)

    class Meta:
        verbose_name = "state"
        verbose_name_plural = "states"

    def __str__(self):
        return self.state

class Devices (models.Model):
    identificador = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50,unique= True)
    modelo = models.CharField(max_length=50)
    AM = models.ForeignKey(AM, on_delete= models.CASCADE)
    partner = models.CharField(max_length=50)
    responsable = models.CharField(max_length=25)
    cliente = models.CharField(max_length=50)
    contacto = models.CharField(max_length=30)
    correo_contacto = models.EmailField(max_length=40)
    Fprestamo = models.DateTimeField()
    Fentrega = models.DateTimeField()
    estado = models.ForeignKey(estado,on_delete= models.CASCADE)
    codigo_prestamo = models.IntegerField()


    
    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.modelo