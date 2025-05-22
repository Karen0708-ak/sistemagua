#importando el modelo cargo
from .models import Casa
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoCasa=Casa.objects.all()
    return render(request,"inicioca.html",{'casa':listadoCasa})

def nuevaCasa(request):
    return render(request,"nuevaCasa.html")
#Almacenando los datos de cargo en la Bdd
def guardarCasa(request):
    direccion = request.POST["direccion"]
    propietario = request.POST["propietario"]
    telefono = request.POST["telefono"]
    nuevoCasa=Casa.objects.create(
            direccion=direccion,
            propietario=propietario,
            telefono=telefono,
        )
    #mensaje de confirmacion
    messages.success(request,"Casa guardado exitosamente")
    return redirect('inicioca')
def eliminarCasa(request,id):
    casaEliminar = Casa.objects.get(id=id)
    casaEliminar.delete()
    messages.success(request,"Casa ELIMINADO exitosamente")
    return redirect('inicioca')

#editar
def editarCasa(request,id):
    casaEditar=Casa.objects.get(id=id)
    return render(request,"editarCasa.html",{'casaEditar':casaEditar})

def procesarEdicionCasa(request):
    id=request.POST["id"]
    direccion = request.POST["direccion"]
    propietario = request.POST["propietario"]
    telefono = request.POST["telefono"]
    casa=Casa.objects.get(id=id)
    casa.direccion=direccion
    casa.propietario=propietario
    casa.telefono=telefono
    casa.save()
    #mensaje de confirmacion
    messages.success(request,"Casa ACTUALIZADO exitosamente")
    return redirect('inicioca')