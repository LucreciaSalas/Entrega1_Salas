from django import forms


class Formulario_pacientes(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad= forms.IntegerField()
    dni= forms.IntegerField()
    patologia= forms.CharField(max_length=40)
    talla= forms.IntegerField()
    peso= forms.IntegerField()
    contorno= forms.IntegerField()

class Formulario_prestadores(forms.Form):
    nombre = forms.CharField(max_length=40)
    especialidad= forms.CharField(max_length=40)
    
class Formulario_proveedores(forms.Form):
    nombre = forms.CharField(max_length=40)
    cuit= forms.IntegerField()
    cbu= forms.IntegerField()    