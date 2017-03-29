from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
@login_required()
def index_encargado(request):
	return render(request, 'index_encargado.html')

@login_required()
def ver_grado(request):
	return render(request, 'ver_grado.html')

@login_required()
def ver_notas(request):
	return render(request, 'ver_notas.html')

@login_required()
def ver_matricula(request):
	return render(request, 'ver_matricula.html')

@login_required()
def ver_historial(request):
	return render(request, 'ver_historial.html')

@login_required()
def ver_historial_alumno(request):
	return render(request, 'ver_historial_alumno.html')

@login_required()
def ver_notas_alumno(request):
	return render(request, 'ver_notas_alumno.html')

@login_required()
def ver_alumnos(request):
	return render(request, 'ver_alumnos.html')

@login_required()
def ver_docente(request):
	return render(request, 'ver_docente.html')
