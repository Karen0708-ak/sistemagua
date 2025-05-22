# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('inicioin',views.inicio,name='inicioin'),
    path('nuevaInstalacion',views.nuevaInstalacion),
    path('guardarInstalacion',views.guardarInstalacion),
    path('eliminarInstalacion/<id>',views.eliminarInstalacion),
    path('editarInstalacion/<id>',views.editarInstalacion),
    path('procesarEdicionInstalacion',views.procesarEdicionInstalacion),
]