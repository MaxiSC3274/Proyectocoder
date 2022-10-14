from django.urls import path
from Appcoder import viewsf
from Appcoder.viewsf import inicio,cursos,servicios,crear_familiar,cursoformulario,formularioh,busquedacamada,buscar

urlpatterns = [
   
    #path('',saludo),
    #path('saludo_con_template/', saludo_con_template),
    #path('',Pagina),
    #path("inicio",inicio),
    path("inicio/", inicio ,name= "inicio"),
    path("servicios/", servicios ,name= "servicios"),
    path("cursos/", cursos ,name= "cursos"),
    path("crear_familiar/", crear_familiar ,name= "crear_familiar"),
    path("cursoformulario/", cursoformulario ,name= "cursoformulario"),
    path("formularioh/", formularioh ,name= "formularioh"),
    path("busquedacamada/", busquedacamada ,name= "busquedacamada"),
    path("buscar/", buscar ,name= "buscar"),
]
