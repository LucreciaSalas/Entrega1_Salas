from django.urls import path
from . import views

urlpatterns = [

    path("", views.inicio),
    path("pacientes", views.pacientes, name="pacientes"),
    path("prestadores", views.prestadores, name="prestadores"),
    path("proveedores", views.proveedores, name="proveedores"),
    #path("lista_pacientes", views.lista_pacientes),
    #path("lista_prestadores", views.lista_prestadores),
    #path("lista_proveedores", views.lista_proveedores),
    #path("alta_pacientes", views.alta_pacientes),
    path("alta_pacientes", views.formulario_pacientes),
    path("alta_prestadores", views.formulario_prestadores),
    path("alta_proveedores", views.formulario_proveedores),
    path("buscar_prestador", views.buscar_prestador),
    path("buscar", views.buscar)
]