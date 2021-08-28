from django.urls import path
from Historial_Costa_Rica import views


urlpatterns = [

    path('', views.historial, name= "Historial_CR"),
    path('historial_CR/<int:equipo_id>', views.agregar, name = "Tabla_CR" ),
    path('buscar_historial_CR', views.buscar_historial,name= "buscar_historial_CR"),
    ]