from django.contrib import admin
from Laboratorio.models import * 
# Register your models here.

class Device_labAdmin(admin.ModelAdmin):
    search_fields=('serial_number','modelo')
    list_display= ('identificador','serial_number','modelo','ubicacion','area')

admin.site.register(Devices_Lab,Device_labAdmin)
admin.site.register(estado_lab)
admin.site.register(sector)

