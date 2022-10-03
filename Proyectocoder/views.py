from django.http import HttpResponse
def saludo(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")