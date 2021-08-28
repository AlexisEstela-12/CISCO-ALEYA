from django.contrib import admin
from Prestamos.models import * 
# Register your models here.


class AMAdmin(admin.ModelAdmin):
    list_display=("nombre","telf","email")
    search_fields=("nombre","email")

class DeviceAdmin(admin.ModelAdmin):
    search_fields=('serial_number','modelo','partner')

admin.site.register(AM,AMAdmin)
admin.site.register(estado)
admin.site.register(Devices,DeviceAdmin)


