from django.urls import path
from Appcoder import viewsf
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from Appcoder.viewsf import (
editarcurso, 
inicio,
cursos,
servicios,
crear_familiar,
cursoformulario,
formularioh,
busquedacamada,
buscar,
leeralumnos,
eliminarcurso,
editarcurso,
listar_cursos,
login_request,
register,
Loginok,
Logout,
editarperfil
)
   

urlpatterns = [
   
    
    path("inicio/", inicio ,name= "inicio"),
    path("EditarBD/", servicios ,name= "servicios"),
    path("cursos/", cursos ,name= "cursos"),
    path("crear_familiar/", crear_familiar ,name= "crear_familiar"),
    path("cursoformulario/", cursoformulario ,name= "cursoformulario"),
    path("formularioh/", formularioh ,name= "formularioh"),
    path("busquedacamada/", busquedacamada ,name= "busquedacamada"),
    path("buscar/", buscar ,name= "buscar"),
    path("leeralumnos/", leeralumnos ,name= "leeralumnos"),
    path('eliminarcurso/<c_nombre>/', eliminarcurso ,name= "EliminarCurso"),
    path('editarcurso/<curso_nombre>/', editarcurso ,name= "EditarCurso"),
    path('listar_cursos/', listar_cursos ,name= "listar_cursos"),
    path('Login/', login_request,name= "Login"),
    path('register/', register,name= "Register"),
    path('Loginok/', Loginok,name= "Loginok"),
    path('Logout/', LogoutView.as_view(template_name='Appcoder/Logout.html'),name= "Logout"),
    path('editarperfil/', editarperfil,name= "EditarPerfil"),

    #path('curso/list', CursoList.as_view() ,name= "CursoList"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)