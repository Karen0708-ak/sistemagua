#importando el modelo cargo
from .models import Empleado
from .models import Casa
from .models import InstalacionCaptacion

from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoInstalacionCaptacion=InstalacionCaptacion.objects.all()
    return render(request,"inicioin.html",{'instalacion':listadoInstalacionCaptacion})

def nuevaInstalacion(request):
    rempleados=Empleado.objects.all()
    lcasa=Casa.objects.all()
    return render(request,"nuevaInstalacion.html",{'empleados':rempleados,'casas':lcasa})
#Almacenando los datos de cargo en la Bdd
def guardarInstalacion(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    empleadoid = request.POST["empleado"]
    empleado = Empleado.objects.get(id=empleadoid)
    casaid = request.POST["casa"]
    casa = Casa.objects.get(id=casaid)
    nuevaInstalacion=InstalacionCaptacion.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            empleado=empleado,
            casa=casa,
        )
    #mensaje de confirmacion
    messages.success(request,"Instalacion guardada exitosamente")
    return redirect('inicioin')

def eliminarInstalacion(request,id):
    instalacionEliminar = InstalacionCaptacion.objects.get(id=id)
    instalacionEliminar.delete()
    messages.success(request,"Instalacion ELIMINADA exitosamente")
    return redirect('inicioin')

#editar
def editarInstalacion(request,id):
    instalacionEditar=InstalacionCaptacion.objects.get(id=id)
    rempleados=Empleado.objects.all()
    lcasa=Casa.objects.all()
    return render(request,"editarInstalacion.html",{'instalacionEditar':instalacionEditar, 'empleados':rempleados,'casas':lcasa})

def procesarEdicionInstalacion(request):
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    empleadoid = request.POST["empleado"]
    empleado = Empleado.objects.get(id=empleadoid)
    casaid = request.POST["casa"]
    casa = Casa.objects.get(id=casaid)
    instalacion=InstalacionCaptacion.objects.get(id=id)
    instalacion.nombre=nombre
    instalacion.descripcion=descripcion
    instalacion.fecha_inicio= fecha_inicio
    instalacion.fecha_fin= fecha_fin
    instalacion.empleado= empleado
    instalacion.casa= casa
    instalacion.save()
    #mensaje de confirmacion
    messages.success(request,"Instalacion ACTUALIZADa exitosamente")
    return redirect('inicioin')