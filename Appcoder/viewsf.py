import http
from pickle import TRUE
from re import A
from tkinter.font import families
from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import  cursomodel
from django.template import loader
from Appcoder.forms import Cursoformulario
from Appcoder.forms import UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatedos = loader.get_template("Inicio.html")
    resdos = templatedos.render()
    return HttpResponse(resdos)


def Loginok(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatelogok = loader.get_template("Loginok.html")
    logok =templatelogok.render()
    return HttpResponse(logok)


def Logout(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatelogok = loader.get_template("Loginok.html")
    logok =templatelogok.render()
    return HttpResponse(logok)    

def servicios(request):
       leercurso = cursomodel.objects.all()
       contextoleer = {"curso": leercurso}     
       return render (request, "Appcoder/leeralumnos.html",contextoleer)

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
          return render(request,"Appcoder/cursoformulario.html")
          
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

def curso(request):

      curso = cursomodel(nombre="Maria antonieta", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)   


def cursos(request):

      if request.method == 'POST':

            miFormulario = Cursoformulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = cursomodel(nombre=informacion['nombre'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= Cursoformulario(initial={'nombre':curso.nombre,'camada':curso.camada}) #Formulario vacio para construir el html
  
      return render (request,"Appcoder/cursoformulario.html", {"miformulario":miFormulario})
        



def formularioh(request):
    #return HttpResponse("hola mundo")
    #return render(request, "Appcoder/Inicio.html")    
    templatefhijo = loader.get_template("Appcoder/formulariohijo.html")
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

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = cursomodel.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/resultadobusqueda.html", {"cursos":cursos, "camada":camada})

      else: 
         
	      return HttpResponse("No enviaste datos") 


      #No olvidar from django.http import HttpResponse
      
def leeralumnos(request):
    leercurso = cursomodel.objects.all()
    contextoleer = {"curso": leercurso}     
    return render (request, "Appcoder/leeralumnos.html",contextoleer)

def eliminarcurso(request,c_nombre):
    #return HttpResponse("holi")
    curso = cursomodel.objects.filter(nombre=c_nombre)
    curso.delete()

    #volver al menu
    leercursodeleted = cursomodel.objects.all()
    contexto = {"cursodelete": leercursodeleted}   
    return render (request, "Appcoder/eliminarcurso.html",contexto) 

def listar_cursos(request):
    todos_los_cursos = cursomodel.objects.all()
    contexto={"cursos_encontrados":todos_los_cursos}
    
    return render(request,"Appcoder/listar-cursos.html", contexto)    

@login_required
def editarcurso(request,curso_nombre):
  
    cursoedit= cursomodel.objects.get(nombre=curso_nombre)
   
    if request.method == 'POST':
       miFormulario = Cursoformulario(request.POST)
       print(miFormulario)
       
       if miFormulario.is_valid:
          
          informacion= miFormulario.cleaned_data
  
          cursoedit.nombre = informacion['nombre']
          cursoedit.camada = informacion['camada']
          cursoedit.save()
  
          return render(request,"Loginok.html")
    else:
          miFormulario = Cursoformulario(initial={'nombre':cursoedit.nombre,'camada':cursoedit.camada})
    return render(request,"Appcoder/editarcurso.html",{"miFormulario":miFormulario,"curso_nombre":curso_nombre})


def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)  
     
        if form.is_valid():
            
             usuario = form.cleaned_data.get('username')
             contra = form.cleaned_data.get('password')

             user= authenticate(username=usuario, password=contra)

             if user is not None:
                 login(request,user)
                 
                 return render(request, "Loginok.html")
             else:
                return render(request,"Loginerror.html")
        else:
                return render(request, "Loginerror.html")
    form = AuthenticationForm()
    return render (request, "Appcoder/login.html", {'form': form})                        

def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse("usuario exitosamente creado")

    else: 
        form = UserCreationForm()
        #form = UserRegisterForm()

    return render(request, "Appcoder/registro.html" , {"form":form})    

def editarperfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            usuario.Email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save
            return render(request, "Appcoder/Loginok.html")
    else:
        miFormulario=UserEditForm(initial={'email': usuario.email})   
    return render (request, "Appcoder/editarperfil.html", {"miFormulario":miFormulario,"usuario":usuario})         
