from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Familiar
from django.template import loader

def crear_familiar(request):
    template = loader.get_template("templatesf.html")

    familiar_1 = Familiar(nombre="Ricardo", apellido = "Hernadez", Edad = 64, Profesion = "Albañil")
    familiar_2 = Familiar(nombre="Javier", apellido = "Hernadez", Edad = 52, Profesion = "Empleado")
    familiar_3 = Familiar(nombre="Carina", apellido = "SantaCruz", Edad = 35, Profesion = "Medica")

    dict_de_contexto = {
        "familias": [familiar_1.nombre,familiar_1.apellido,familiar_1.Edad,familiar_1.Profesion],
        "familiasdos": [familiar_2.nombre,familiar_2.apellido,familiar_2.Edad,familiar_2.Profesion],
        "familiastres": [familiar_3.nombre,familiar_3.apellido,familiar_3.Edad,familiar_3.Profesion],

    }
    print(dict_de_contexto)

    res = template.render(dict_de_contexto)

    return HttpResponse(res)