
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from Laboratorio_Costa_Rica import views

urlpatterns = [
    path('',views.Laboratorio, name= "Laboratorio_CR"),
    path('buscar_CR/',views.buscar, name= "Busqueda_CR"),
    path('devolver_CR/<int:equipo_id>', views.agregar_elemento, name = "Devolver_CR" ),
]

# urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)