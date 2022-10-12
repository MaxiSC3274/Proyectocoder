import http
from pickle import TRUE
from tkinter.font import families
from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import  estudiante, cursomodel, camadamodel
from django.template import loader
from Appcoder.forms import Cursoformulario, formulariohijo


def inicio(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatedos = loader.get_template("Inicio.html")
    resdos = templatedos.render()
    return HttpResponse(resdos)

def servicios(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Servicios.html")    
    templatefour = loader.get_template("Servicios.html")
    resfour = templatefour.render()
    return HttpResponse(resfour)     

def cursoformulario(request):
   
    if request.method == "GET":
       mi_formulario = Cursoformulario()
       contexto={"formulario":mi_formulario}
       return render(request,"Appcoder/formulariohijo.html",context=contexto)
    
    
    if request.method =="POST":
       mi_formulario = Cursoformulario(request.POST)    
       if mi_formulario.is_valid():
          #mi_formulario.save()
          datos_ingresados = mi_formulario.cleaned_data
          nuevo_model = cursomodel(
          nombre=datos_ingresados["nombre"],
            #curso =datos_ingresados["curso"],
          camada =datos_ingresados["camada"],
          )
          
          nuevo_model.save()  
          return HttpResponse("guardado") 
    #return render(request,"Appcoder/cursoformulario.html")
    else:
          return render(request,"Appcoder/cursoformulario.html")
    mi_formulario=Cursoformulario()
    return render (request,"Appcoder/cursoformulario.html",{"miformulario":mi_formulario})

 #contexto = {"formulario": mi_formulario}
 #return render (request, "Appcoder/cursoformulario.html", context= contexto)


    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Servicios.html")    
    #templatefive = loader.get_template("cursoformulario.html")
    #resfive = templatefive.render()
    #return HttpResponse(resfive)    
    #if request.method != 'POST':
        #return HttpResponse("eyyy")
       # return render(request,"Appcoder/cursoformulario.html")
    
   # curso = cursomodel (nombre=request.POST["curso"], camada=request.POST["camada"])
    #curso.save
    #return render(request, "Inicio.html")
   

def cursos(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    #templatetres = loader.get_template("Cursos.html")
    #restres = templatetres.render()
    #return HttpResponse(restres)    

    if request.method =='POST':
       miFormulario = Cursoformulario(request.POST)
       print(miFormulario)

       if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          curso = cursomodel(nombre=informacion['curso'],camada=informacion['camada'])
          curso.save()
          return render(request, "Appcoder/inicio.html")

    else:
        miFormulario=Cursoformulario()

    return render(request , "Appcoder/cursos.html"), {"miFormulario":miFormulario}          



def formularioh(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatefhijo = loader.get_template("Appcoder/curso.html")
    resfhijo = templatefhijo.render()
    return HttpResponse(resfhijo)   
   
    

def crear_familiar(request):
    template = loader.get_template("templatesf.html")

    familiar_1 = cursomodel(nombre="RicardoRuben",camada = 64)#curso= "Biologia", 
    familiar_2 = cursomodel(nombre="JavierInsua",camada = 52 )# curso= "FisioterapiaDos", 
    familiar_3 = cursomodel(nombre="CarinaCarola",camada = 35 )# curso= "PianoAPB", 

    dict_de_contexto = {
        "familias": [familiar_1.nombre,familiar_1.camada],#familiar_1.curso,
        "familiasdos": [familiar_2.nombre,familiar_2.camada],#familiar_2.curso,
        "familiastres": [familiar_3.nombre,familiar_3.camada],#familiar_3.curso,

    }
    print(dict_de_contexto)

    res = template.render(dict_de_contexto)

    return HttpResponse(res)

def busquedacamada(request):
    return render(request,"Appcoder/busquedacamada.html")

def buscar(request):
    #respuesta=f"Estoy buscando la camada numero:{request.GET['camada']}"
    #return HttpResponse(respuesta)
    if request.GET["camada"]:

       camada = request.GET['camada'] 
       cursos = cursomodel.objects.filter(camada_icontains=camada)

       return render(request, "Appcoder/resultadobusqueda.html",{"cursos":cursos, "camada":camada})
    else:
       respuesta ="no enviaste nada"   
    return HttpResponse(respuesta)   
