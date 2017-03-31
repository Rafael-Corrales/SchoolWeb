from django.contrib import admin

from .models import *

admin.site.register(Perfil)
admin.site.register(Grado)
admin.site.register(Seccion)
admin.site.register(GradoSeccion)
admin.site.register(Clase)
admin.site.register(GradoClase)
admin.site.register(Anio)
admin.site.register(OfertaGrado)
admin.site.register(Sexo)
admin.site.register(EstadoClase)
admin.site.register(EstadoAlumno)
admin.site.register(Alumno)
admin.site.register(EncargadoAlumno)
admin.site.register(OfertaClase)
admin.site.register(Matricula)
admin.site.register(DetalleMatricula)
admin.site.register(Configuracion)

