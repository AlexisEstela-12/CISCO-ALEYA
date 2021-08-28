from django.urls import path
from Prestamos_Costa_Rica import views




urlpatterns = [

    path('', views.funcion_prestar, name= "Prestamos_CR"),
    path('pedido_CR/<int:id>', views.Nuevo_Prestamo, name = "Pedido_CR" ),
    path('buscar_CR/',views.buscar_prestamos,name= "Busqueda_prestamo_CR")

    ]