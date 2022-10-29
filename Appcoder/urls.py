from django.urls import path
from Appcoder import viewsf
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
    #path('curso/list', CursoList.as_view() ,name= "CursoList"),
]
