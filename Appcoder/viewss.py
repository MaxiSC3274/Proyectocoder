from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

#def saludo(request):
    #return HttpResponse("<h1>Hola Mundo!</h1>")

#from django.http import HttpResponse


def Pagina(request):
 
    Familiares=Familiar.objects.all()
    return render(request,"familiares.html",{"nombres":Familiares})

