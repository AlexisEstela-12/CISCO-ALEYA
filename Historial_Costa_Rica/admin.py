from django.contrib import admin
from Historial_Costa_Rica.models import *

# Register your models here.


class Device_admin(admin.ModelAdmin):
    search_fields = ('serial_number','modelo','partner','AM')


admin.site.register(Devices_Historial,Device_admin)