# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('inicioca',views.inicio,name='inicioca'),
    path('nuevaCasa',views.nuevaCasa),
    path('guardarCasa',views.guardarCasa),
    path('eliminarCasa/<id>',views.eliminarCasa),
    path('editarCasa/<id>',views.editarCasa),
    path('procesarEdicionCasa',views.procesarEdicionCasa),
]