from django.urls import path
from Historial import views


urlpatterns = [

    path('', views.historial, name= "Historial"),
    path('historial/<int:equipo_id>', views.agregar, name = "Tabla" ),
    path('buscar_historial', views.buscar_historial,name= "buscar_historial"),
    ]