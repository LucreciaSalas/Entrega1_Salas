from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import *
from django.template import loader
from app_coder.forms import *


# Create your views here.

def inicio(request): 
    return render(request, "plantillas.html")

def pacientes(request):
    pacientes= Pacientes.objects.all()
    datos= {"pacientes" : pacientes }
    plantilla= loader.get_template("pacientes.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

def prestadores(request):
    prestadores= Prestadores.objects.all()
    datos= {"prestadores" : prestadores }
    plantilla= loader.get_template("prestadores.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

def proveedores(request):
    proveedores= Proveedores.objects.all()
    datos= {"proveedores" : prestadores }
    plantilla= loader.get_template("proveedores.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

def formulario_pacientes (request):
    if request.method == "POST":
        
        mi_formulario= Formulario_pacientes(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            pacientes = Pacientes( nombre=datos['nombre'] , edad=datos['edad'] , dni=datos['dni'] , patologia=datos['patologia'] , talla=datos['talla'] , peso=datos['peso'] , contorno=datos['contorno']) 
            pacientes.save()
        return render (request , "formpacientes.html")
    return render (request , "formpacientes.html")


def formulario_proveedores (request):
    if request.method == "POST":
        proveedores = Proveedores( nombre=request.POST['nombre'] , cuit=request.POST['cuit'] , cbu=request.POST['cbu']) 
        proveedores.save()
        return render (request , "formproveedores.html")
    return render (request , "formproveedores.html")

def formulario_prestadores (request):
    if request.method == "POST":
        prestadores = Prestadores( nombre=request.POST['nombre'] , especialidad=request.POST['especialidad']) 
        prestadores.save()
        return render (request , "formprestadores.html")
    return render (request , "formprestadores.html")
    

def buscar_prestador(request):
    return render(request, "buscar_prestador.html")

def buscar(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        prestadores= Prestadores.objects.filter(nombre__icontains= nombre)
        return render (request, "resultado_busqueda.html", {"prestadores": prestadores})
    else:
        return HttpResponse("Campo vacio")     
   



# def lista_pacientes(request):                   #función configurada en clase 18 HORA 1:48#
#    pacientes= Pacientes.objects.all()
#   datos= {"datos" : pacientes }
#    plantilla= loader.get_template("plantillas.html")
#   documento= plantilla.render(datos)
#   return HttpResponse(documento)

# def lista_prestadores(request):
#    prestadores= Prestadores.objects.all()
#    return HttpResponse (prestadores)

# def lista_proveedores(request):
#    proveedores= Proveedores.objects.all()
#    return HttpResponse (proveedores)
    
#  FALTA CONFIGURAR INGRESO POR FORMULARIO #
# def alta_pacientes (request):
#    paciente= Pacientes(nombre="María Laura Perez", edad=30, dni=38555678,  patologia="diabetes", talla=170, peso=70, contorno=80)
#    paciente.save()
#   paciente= Pacientes(nombre="Pedro Gutierrez", edad=67, dni=8577087,  patologia="diabetes", talla=180, peso=110, contorno=140)
#   paciente.save()
    
#    return HttpResponse("Se ha cargado lista de pacientes")

