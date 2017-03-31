from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from admini.models import *

from django.contrib.auth.models import User
@login_required()
def index_encargado(request):
	if request.user.Perfil.es_tutor:
		return render(request, 'index_encargado.html')
	else:
		return render(request, 'denegado.html')

@login_required()
def ver_grado(request, ida):
	if request.user.Perfil.es_tutor:
		alu = Alumno.objects.get(pk = ida)
		gra = Matricula.objects.filter(alumno = alu)
		return render(request, 'ver_grado.html', {'gra': gra})
	else:
		return render(request, 'denegado.html')

# @login_required()
# def ver_notas(request):
# 	if request.user.Perfil.es_tutor:
# 		return render(request, 'ver_notas.html')

@login_required()
def ver_matricula(request, ida):
	if request.user.Perfil.es_tutor:
		alu = Alumno.objects.get(pk = ida)
		matri = Matricula.objects.get(alumno = alu)
		return render(request, 'ver_matricula.html', {'matri': matri})
	else:
		return render(request, 'denegado.html')

# @login_required()
# def ver_historial(request):
# 	if request.user.Perfil.es_tutor:
# 		return render(request, 'ver_historial.html')

@login_required()
def ver_historial_alumno(request):
	if request.user.Perfil.es_tutor:
		return render(request, 'ver_historial_alumno.html')
	else:
		return render(request, 'denegado.html')

@login_required()
def ver_notas_alumno(request, ida):
	if request.user.Perfil.es_tutor:
		alu = Alumno.objects.get(pk = ida)
		matri = Matricula.objects.get(alumno = alu)
		notas = DetalleMatricula.objects.get(matricula = matri)
		return render(request, 'ver_notas_alumno.html', {'notas': notas})
	else:
		return render(request, 'denegado.html')

@login_required()
def ver_alumnos(request):
	if request.user.Perfil.es_tutor:
		alu = EncargadoAlumno.objects.filter(encargado = request.user)
		return render(request, 'ver_alumnos.html', {'alu': alu})
	else:
		return render(request, 'denegado.html')

@login_required()
def ver_docente(request, ida):
	if request.user.Perfil.es_tutor:
		alu = Alumno.objects.get(pk = ida)
		matri = Matricula.objects.get(alumno = alu)
		og = OfertaGrado.objects.get(pk = matri.ofertagrado.id)
		oc = OfertaClase.objects.filter(ofertagrado = og)
		return render(request, 'ver_docente.html', {'oc': oc})
	else:
		return render(request, 'denegado.html')
