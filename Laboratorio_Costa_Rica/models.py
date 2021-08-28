from django.db import models

# Create your models here.


class estado_lab(models.Model):
    state=models.CharField(max_length=15)

    class Meta:
        verbose_name = "state"
        verbose_name_plural = "states"

    def __str__(self):
        return self.state


class sector(models.Model):
    sec = models.CharField(max_length=20)

    class Meta:
        verbose_name = "sector"
        verbose_name_plural = "sectores"

    def __str__(self):
        return self.sec

class Devices_Lab (models.Model):
    identificador = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50,unique=True)
    modelo = models.CharField(max_length=50)
    estado = models.ForeignKey(estado_lab,on_delete= models.CASCADE)
    ubicacion = models.CharField(max_length=30)
    area = models.ForeignKey(sector,on_delete=models.CASCADE,default="Collaboration")


    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.modelo