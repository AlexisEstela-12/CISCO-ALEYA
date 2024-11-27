from django.urls import path
from Prestamos import views

urlpatterns = [

    path('', views.funcion_prestar, name= "Prestamos"),
    path('pedido/<int:id>', views.Nuevo_Prestamo, name = "Pedido" ),
    path('buscar_prestamo/',views.buscar_prestamos,name= "Busqueda_prestamo")

    ]