from django.urls import re_path
from django.urls import path
from Laboratorio import views

urlpatterns = [
    path('', views.Laboratorio, name= "Laboratorio"),
    path('buscar/',views.buscar, name= "Busqueda"),
    path('devolver/<int:equipo_id>', views.agregar_elemento, name = "Devolver" ),

   
]

