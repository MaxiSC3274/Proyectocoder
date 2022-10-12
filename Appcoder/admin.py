from django.contrib import admin

from Appcoder.models import estudiante, cursomodel, camadamodel

# Register your models here.

admin.site.register(cursomodel)
admin.site.register(camadamodel)
admin.site.register(estudiante)

